from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor

from model import FileInfoData,Data
from config.table import Column,Palette,ColumnNumber,COLUMN_COUNT

import time


class FileTableModel(QAbstractTableModel):

    def __init__(self, files: Data):

        super(FileTableModel, self).__init__()

        self.files: list[FileInfoData] = sorted(files, key=lambda x: x.file_hash)
        self.hash_colors = self.assign_colors()

    def assign_colors(self):

        colors = {}
        pastel_colors = Palette.pastel
        hash_list = list(dict.fromkeys([ i.file_hash for i in self.files]))
        
        for i, fhash in enumerate(hash_list):
            if fhash not in colors:
                colors[fhash] = pastel_colors[i % len(pastel_colors)]  
        del hash_list
                
        return colors

    def rowCount(self, parent=None):

        return len(self.files)

    def columnCount(self, parent=None):

        return COLUMN_COUNT  

    def data(self, index, role):

        file = self.files[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == ColumnNumber.PATH:
                return file.path
            elif index.column() == ColumnNumber.NAME:
                return file.name
            elif index.column() == ColumnNumber.CREATIONT:
                return time.ctime(file.creation_time)
            elif index.column() == ColumnNumber.SIZE:
                return file.size
        elif role == Qt.ItemDataRole.ForegroundRole:
            return QColor(Qt.black)
        elif role == Qt.ItemDataRole.BackgroundRole:
            return self.hash_colors[file.file_hash]
        elif role == Qt.ItemDataRole.CheckStateRole and index.column() == ColumnNumber.SELECTED:
            return Qt.CheckState.Checked if file.selected else Qt.CheckState.Unchecked

    def setData(self, index, value, role):

        if (
            index.isValid()
            and role == Qt.ItemDataRole.CheckStateRole
            and index.column() == ColumnNumber.SELECTED
        ):
            if value == Qt.CheckState.Checked.value:
                self.files[index.row()].selected = True
            else:
                self.files[index.row()].selected = False

            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def flags(self, index):

        if index.column() == ColumnNumber.SELECTED:
            return (
                Qt.ItemFlag.ItemIsEnabled
                | Qt.ItemFlag.ItemIsSelectable
                | Qt.ItemFlag.ItemIsUserCheckable
            )
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

    def headerData(self, section, orientation, role):

        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Horizontal:
           
            if section == ColumnNumber.PATH:
                return Column.PATH
            elif section == ColumnNumber.NAME:
                return Column.NAME
            elif section == ColumnNumber.CREATIONT:
                return Column.CREATIONT
            elif section == ColumnNumber.SIZE:
                return Column.SIZE
            elif section == ColumnNumber.SELECTED:
                return Column.SELECTED

    def selected_files(self):

        selected_paths = [file.path for file in self.files if file.selected]
        return selected_paths
    