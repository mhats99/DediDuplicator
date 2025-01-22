from PySide6.QtWidgets import QFileDialog, QMessageBox, QMainWindow

from config.scripts import FolderPathConfig
from config.global_config import CRITICAL_MESSAGE


class FolderPath:

    def __init__(self, base: QMainWindow):

        self.__base = base

    def add(self):

        self.__base.setDisabled(True)
        try:
            while True:
                path = QFileDialog.getExistingDirectory(
                    self.__base, FolderPathConfig.ADD_FILE_DIOLOG_CAPTION
                )
                self.__base.setDisabled(False)

                if path in self.__base._folder_path.get_items():
                    QMessageBox.warning(
                        self.__base,
                        FolderPathConfig.ADD_MESSAGE_BOX_TITLE,
                        FolderPathConfig.ADD_MESSAGE_BOX_TEXT,
                    )

                else:
                    self.__base.ui.listWidget_path.addItem(path)
                    break
        except Exception as e:
            self.__loger.critical(e)
            self.__base._statusbar_message.show_error_message(
                CRITICAL_MESSAGE, FolderPathConfig.CRITICAL_ADD
            )

        self.__base.setDisabled(False)

    def remove(self):

        try:
            selected_items = self.__base.ui.listWidget_path.selectedItems()

            if not selected_items:
                self.__base._statusbar_message.show_warning_message(
                    FolderPathConfig.REMOVE_WARNING_STATUSBAR_MESSAGE,
                    FolderPathConfig.WARNING_STATUSBAR_TIME_OUT,
                )

            else:
                for item in selected_items:
                    self.__base.ui.listWidget_path.takeItem(
                        self.__base.ui.listWidget_path.row(item)
                    )
        except Exception as e:
            self.__loger.critical(e)
            self.__base._statusbar_message.show_error_message(
                CRITICAL_MESSAGE, FolderPathConfig.CRITICAL_REMOVE
            )

    def reset(self):

        self.__base.ui.listWidget_path.clear()
        self.__base._statusbar_message.show_success_message(
            FolderPathConfig.RESET_SUCCESS_STATUSBAR_MESSAGE,
            FolderPathConfig.SUCCESS_STATUSBAR_TIME_OUT,
        )

    def get_items(self) -> list[str]:

        return [
            self.__base.ui.listWidget_path.item(i).text()
            for i in range(self.__base.ui.listWidget_path.count())
        ]
