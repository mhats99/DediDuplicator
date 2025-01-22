# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow

from ui import Ui_MainWindow

from .folder_path import FolderPath
from .scan import Scan
from .delete_options import DeleteOptions
from .info_windows import InfoWindows
from module.ui_tool import StatusbarMessage



class Base(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self._folder_path = FolderPath(self)
        self._scan = Scan(self)
        self._table_model = None
        self._delete_opt = DeleteOptions(self)
        self._statusbar_message = StatusbarMessage(self.ui.statusbar)
        self.__info_w = InfoWindows(self)
        self._open_info = None 

        
        self.ui.pushButton_path_add.clicked.connect(self._folder_path.add)
        self.ui.pushButton_path_remove.clicked.connect(self._folder_path.remove)
        self.ui.toolButton_path_reset.clicked.connect(self._folder_path.reset)

        self.ui.pushButton_deleteOptions_delete.clicked.connect(self._delete_opt.delete)
        self.ui.radioButton_deleteOptions_time_old.clicked.connect(self._delete_opt.select_time)
        self.ui.radioButton_deleteOptions_time_new.clicked.connect(self._delete_opt.select_time)
        
        self.ui.pushButton_scan.clicked.connect(self._scan.go)
        
        self.ui.toolButton_info.clicked.connect(self.__info_w.open)

        