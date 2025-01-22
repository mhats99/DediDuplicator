from PySide6.QtWidgets import QStatusBar
from PySide6.QtCore import QTimer

class StatusbarMessage:
    
    def __init__(self,status_bar: QStatusBar):
        
        self.__status_bar = status_bar
    
    def show_info_message(self, message: str, time_out: int = 0):
        """Show info message."""
        self.__status_bar.showMessage(message,time_out*1000)


    def show_error_message(self, message: str, time_out: int = 0):
        """Show error message.Text color red"""
        self.__status_bar.setStyleSheet("QStatusBar { color: red; }")  
        self.__status_bar.showMessage(message,time_out*1000)

        QTimer.singleShot(time_out * 1000, self.reset_status_bar)


    def show_warning_message(self, message: str, time_out: int = 0):
        """Show warning message.Text color orange"""
        self.__status_bar.setStyleSheet("QStatusBar { color: orange; }")  
        self.__status_bar.showMessage(message, time_out * 1000)

        if time_out > 0:
            QTimer.singleShot(time_out * 1000, self.reset_status_bar)

    def show_success_message(self, message: str, time_out: int = 0):
        """Show success message.Text color green"""
        self.__status_bar.setStyleSheet("QStatusBar { color: green; }")  
        self.__status_bar.showMessage(message, time_out * 1000)

        if time_out > 0:
            QTimer.singleShot(time_out * 1000, self.reset_status_bar)

    def reset_status_bar(self):
        """Reset the status bar text color to default"""
        self.__status_bar.setStyleSheet("")
        self.__status_bar.showMessage("") 
