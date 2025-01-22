from PySide6.QtWidgets import QMessageBox, QMainWindow

from model import Data

from module.ui_tool import Worker
from module import Logger

from processes import copy_find_processes, files_info_worker
from processes import FileTableModel

from config.global_config import LOG_FİLE, CRITICAL_MESSAGE
from config.scripts import ScanConfig

from .table_data_load import table_data_load


class Scan:

    def __init__(self, base: QMainWindow):

        self.__base = base
        self.__data: Data = None
        self.__copy_files_info: Data = None
        self.__worker = Worker()
        self.__logger = Logger(LOG_FİLE)

        self.__worker.signals.progress.connect(self.__update_progress)
        self.__worker.signals.finished.connect(self.__on_finished)
        self.__worker.signals.show_error.connect(self.__show_error)
        self.__worker.signals.error.connect(self.__error)

    def go(self):

        path_list = self.__base._folder_path.get_items()

        if len(path_list) == 0 or None or all(item == "" for item in path_list):

            QMessageBox.warning(
                self.__base,
                ScanConfig.START_MESSAGE_BOX_TITLE,
                ScanConfig.START_MESSAGE_BOX_TEXT,
            )
            return

        else:
            try:
                self.clear_table()
                self.__base.ui.pushButton_scan.setEnabled(False)
                if self.__base.ui.listWidget_delete_file_path.count() > 0:
                    self.__base.ui.listWidget_delete_file_path.clear()
                self.__base._statusbar_message.show_info_message(
                    ScanConfig.START_STATUSBAR_INFO_MESSAGE
                )

                self.__data = Data()
                files_info_worker(
                    self.__worker, path_list, self.__data, self.set_progresbar
                )
            except Exception as e:
                self.__loger.critical(e)
                self.__base._statusbar_message.show_error_message(
                    CRITICAL_MESSAGE, ScanConfig.CRITICAL_START
                )

    def get_copy_files_info(self):

        return self.__copy_files_info

    def set_copy_files_info(self, data: Data):

        self.__copy_files_info = data

    def clear_table(self):

        try:
            self.__data = None
            self.__base._table_model = FileTableModel([])
            self.__base.ui.tableView_result.setModel(self.__base._table_model)
        except Exception as e:
            self.__loger.critical(e)
            self.__base._statusbar_message.show_error_message(
                CRITICAL_MESSAGE, ScanConfig.CRITICAL_CLEAR_TABLE
            )

    def progresbar_reset(self):

        self.set_progresbar(0, 0, 0)

    def set_progresbar(self, minimum: int, maximum: int, value: int):

        self.__base.ui.progressBar_scan.setRange(minimum, maximum)
        self.__base.ui.progressBar_scan.setValue(value)

    def __update_progress(self, value):

        self.__base.ui.progressBar_scan.setValue(value)

    def __on_finished(self, result: list):

        try:
            self.__copy_files_info = copy_find_processes(self.__data)
            self.__base.ui.lcdNumber_duplicate_files.display(
                len(self.__copy_files_info)
            )
            self.__base.ui.pushButton_scan.setEnabled(True)
            self.progresbar_reset()

            if len(self.__copy_files_info) > 0:
                table_data_load(self.__base, self.__copy_files_info)
                self.__base._statusbar_message.show_success_message(
                    ScanConfig.ON_FINISHED_STATUSBAR_SUCCESS_MESSAGE,
                    ScanConfig.SUCCESS_STATUSBAR_TIME_OUT,
                )
            else:
                self.clear_table()
                self.__base._statusbar_message.show_success_message(
                    ScanConfig.ON_FINISHED_STATUSBAR_SUCCESS_MESSAGE_NOT_FILE,
                    ScanConfig.SUCCESS_STATUSBAR_TIME_OUT,
                )
                self.__copy_files_info = None

            if not all(item is None for item in result):
                result = [item is not None for item in result]
                if len(result) > 0:
                    for i in result:
                        self.__logger.error(i)

        except Exception as e:
            self.__loger.critical(e)
            self.__base._statusbar_message.show_error_message(
                CRITICAL_MESSAGE, ScanConfig.CRITICAL_ON_FINISHED
            )

    def __show_error(self, message):

        self.__base._statusbar_message.show_error_message(
            message, ScanConfig.ERROR_STATUSBAR_TIME_OUT
        )

    def __error(self, value: str):
        self.__logger.error(value)
