from PySide6.QtWidgets import QApplication
from scripts import Base
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Base()
    widget.show()
    sys.exit(app.exec())
