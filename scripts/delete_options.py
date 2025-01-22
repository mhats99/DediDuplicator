from PySide6.QtWidgets import QMainWindow, QMessageBox

from model import Data
from module import Logger
from processes import FileDelete

from .table_data_load import table_data_load

from config.global_config import LOG_FİLE, CRITICAL_MESSAGE
from config.scripts import DeleteOptionsConfig


class DeleteOptions:

    def __init__(self, base: QMainWindow):

        self.__base = base
        self.__stime = None
        self.__loger = Logger(LOG_FİLE)

    def delete(self):

        if self.__base._table_model == None:

            QMessageBox.warning(
                self.__base,
                DeleteOptionsConfig.DELETE_MESSAGE_BOX_TITLE,
                DeleteOptionsConfig.DELETE_MESSAGE_BOX_TEXT,
            )
            return

        else:
            self.__base._statusbar_message.show_info_message(
                DeleteOptionsConfig.DELETE_INFO_STATUSBAR_MESSAGE
            )
            self.__base.ui.pushButton_deleteOptions_delete.setEnabled(False)

            self.__del_list = self.__base._table_model.selected_files()

            if len(self.__del_list) == 0:
                self.__finished(None)
                return
            else:
                try:
                    self.__work = FileDelete(self.__del_list)
                    self.__work.signals.error.connect(self.__error)
                    self.__work.signals.finished.connect(self.__finished)
                    self.__work.start()
                except Exception as e:
                    self.__loger.critical(e)
                    self.__base._statusbar_message.show_error_message(
                        CRITICAL_MESSAGE, DeleteOptionsConfig.CRITICAL_DELETE
                    )

    def select_time(self):

        is_new_checked = self.__base.ui.radioButton_deleteOptions_time_new.isChecked()
        is_old_checked = self.__base.ui.radioButton_deleteOptions_time_old.isChecked()

        if (
            (
                (is_new_checked and self.__stime)
                or (is_old_checked and not self.__stime)
                or (not self.__stime)
            )
            and self.__base._table_model
            and type(self.__base._scan.get_copy_files_info()) == Data
        ):
            try:
                if is_new_checked:
                    self.__stime = False
                else:
                    self.__stime = True

                data = self.__base._scan.get_copy_files_info()
                hash_to_list = data.get_grouping_by_hash()
                result = Data()
                del data

                for value in hash_to_list:
                    ct_list = [i.creation_time for i in value]

                    if is_new_checked:
                        ct_list.remove(min(ct_list))
                    elif is_old_checked:
                        ct_list.remove(max(ct_list))

                    for i in value:
                        if i.creation_time in ct_list:
                            i.selected = True
                        else:
                            i.selected = False
                        result.add(i)

                table_data_load(self.__base, result)
                del is_new_checked, is_old_checked

            except Exception as e:
                self.__loger.critical(e)
                self.__base._statusbar_message.show_error_message(
                    CRITICAL_MESSAGE, DeleteOptionsConfig.CRITICAL_SELECT_TIME
                )
        else:
            if not self.__base._table_model:
                self.__base._statusbar_message.show_warning_message(
                    DeleteOptionsConfig.SELECT_TIME_WARNING_STATUSBAR_MESSAGE_NOT_SCAN,
                    DeleteOptionsConfig.WARNING_STATUSBAR_TIME_OUT,
                )
                self.__stime = None

            elif not type(self.__base._scan.get_copy_files_info()) == Data:
                self.__base._statusbar_message.show_warning_message(
                    DeleteOptionsConfig.SELECT_TIME_WARNING_STATUSBAR_MESSAGE_NOT_COPY,
                    DeleteOptionsConfig.WARNING_STATUSBAR_TIME_OUT,
                )
                self.__stime = None

            else:
                self.__base._statusbar_message.show_warning_message(
                    DeleteOptionsConfig.SELECT_TIME_WARNING_STATUSBAR_MESSAGE_SELECT,
                    DeleteOptionsConfig.WARNING_STATUSBAR_TIME_OUT,
                )

    def __error(self, message: str):
        self.__loger.error(message)

    def __finished(self, produce: list[tuple]):

        self.__work = None
        self.__base.ui.pushButton_deleteOptions_delete.setEnabled(True)

        if produce in [(None, False), None]:
            self.__base._statusbar_message.show_warning_message(
                DeleteOptionsConfig.FINISHED_WARNING_STATUSBAR_MESSAGE,
                DeleteOptionsConfig.WARNING_STATUSBAR_TIME_OUT,
            )
            return
        else:
            try:
                file_not_found = []  # (file_path, False)
                file_error = []  # (file_path, False, str(e))
                file_delete = []  # (file_path, True)
                for i in produce:
                    if len(i) == 3:
                        file_error.append(i)
                    elif i[1]:
                        file_delete.append(i[0])
                    else:
                        file_not_found.append(i[0])

                data = self.__base._scan.get_copy_files_info()

                if len(file_not_found) > 0:
                    data.set_data(
                        list(set(data) - set(data.get_path_to_info(file_not_found)))
                    )

                if len(file_error) > 0:

                    self.__base.ui.listWidget_delete_file_path.addItems(
                        [i[0] for i in file_error]
                    )
                    self.__base._statusbar_message.show_error_message(
                        DeleteOptionsConfig.FINISHED_ERROR_STATUSBAR_MESSAGE_UNDELETABLE_FILE,
                        DeleteOptionsConfig.ERROR_STATUSBAR_TIME_OUT,
                    )

                    for error in file_error:
                        self.__loger.error(error[2], error[0])

                result = Data()
                result.set_data(
                    list(set(data) - set(data.get_path_to_info(file_delete)))
                )
                del file_delete
                x = [
                    file
                    for sublist in result.get_grouping_by_hash()
                    if len(sublist) > 1
                    for file in sublist
                ]
                if not x:
                    self.__base._scan.clear_table()
                    self.__base._scan.set_copy_files_info(Data())
                    self.__base.ui.lcdNumber_duplicate_files.display(0)
                    self.__base._statusbar_message.show_success_message(
                        DeleteOptionsConfig.FINISHED_SUCCESS_STATUSBAR_MESSAGE_ALL,
                        DeleteOptionsConfig.SUCCESS_STATUSBAR_TIME_OUT,
                    )
                else:
                    self.__base.ui.lcdNumber_duplicate_files.display(len(x))
                    result.set_data(x)
                    self.__base._scan.set_copy_files_info(result)
                    table_data_load(self.__base, result)
                    self.__base._statusbar_message.show_success_message(
                        DeleteOptionsConfig.FINISHED_SUCCESS_STATUSBAR_MESSAGE_SELECTED,
                        DeleteOptionsConfig.SUCCESS_STATUSBAR_TIME_OUT,
                    )
            except Exception as e:
                self.__loger.critical(e)
                self.__base._statusbar_message.show_error_message(
                    CRITICAL_MESSAGE, DeleteOptionsConfig.CRITICAL_FINISHED
                )
