from processes import FileTableModel
from model import FileInfoData
from PySide6.QtWidgets import QMainWindow


def table_data_load(base:QMainWindow,data:list[FileInfoData]):
    
    base._table_model = FileTableModel(data)
    base.ui.tableView_result.setModel(base._table_model)
    base.ui.tableView_result.resizeRowsToContents()
    for i in range(2,base._table_model.columnCount()-1):
        base.ui.tableView_result.resizeColumnToContents(i)
    