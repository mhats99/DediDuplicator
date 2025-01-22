from PySide6.QtCore import QThread, QObject, Signal
from module import FileTool


class DelteSignals(QObject):

    finished = Signal(list)
    error = Signal(str)


class FileDelete(QThread):

    def __init__(self, path_list: list[str]):

        super().__init__()
        self.__path_list = path_list
        self.signals = DelteSignals()

    def run(self):

        try:
            result = FileTool.delete_files(self.__path_list)
            self.signals.finished.emit(result)
        except Exception as e:
            self.signals.error.emit(str(e))
