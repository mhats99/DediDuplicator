from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal 

from ui import Ui_info

class Info(QWidget):
    
    close_window = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_info()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.exit)
    
    def exit(self):
        
        self.close_window.emit(True) 
        self.close()

    def closeEvent(self, event):
        
        self.close_window.emit(True) 
        event.accept()
   