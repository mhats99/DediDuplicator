from PySide6.QtGui import QColor


class Column:

    HASH: str = "Hash"
    PATH: str = "Path"
    NAME: str = "Name"
    CREATIONT: str = "Creation Time"
    SIZE: str = "Size"
    SELECTED: str = "Selected"


class ColumnNumber:

    PATH: int = 0
    NAME: int = 1
    CREATIONT: int = 2
    SIZE: int = 3
    SELECTED: int = 4


COLUMN_COUNT: int = 5


class Palette:

    dark: list[QColor] = [
        QColor(45, 45, 48),  # Anthracite
        QColor(63, 81, 181),  # Indigo
        QColor(229, 57, 53),  # Red
        QColor(56, 142, 60),  # Green
        QColor(255, 193, 7),  # Amber
        QColor(38, 198, 218),  # Turquoise
        QColor(171, 71, 188),  # Purple
        QColor(255, 87, 34),  # Orange
        QColor(255, 235, 59),  # Yellow
        QColor(0, 188, 212),  # Cyan
    ]

    light: list[QColor] = [
        QColor(220, 220, 220),  # Gray
        QColor(66, 165, 245),  # Light Blue
        QColor(239, 83, 80),  # Red
        QColor(102, 187, 106),  # Green
        QColor(255, 238, 88),  # Amber
        QColor(77, 208, 225),  # Turquoise
        QColor(186, 104, 200),  # Purple
        QColor(255, 112, 67),  # Orange
        QColor(255, 241, 118),  # Yellow
        QColor(79, 195, 247),  # Cyan
    ]

    pastel: list[QColor] = [
        QColor(255, 182, 193),  # Pink
        QColor(173, 216, 230),  # Light Blue
        QColor(255, 160, 122),  # Coral
        QColor(152, 251, 152),  # Light green
        QColor(255, 255, 204),  # Light Yellow
        QColor(176, 224, 230),  # Baby Blue
        QColor(221, 160, 221),  # Plum Blossom
        QColor(255, 228, 196),  # Wheat
        QColor(250, 235, 215),  # Antique White
        QColor(255, 228, 181),  # Corn Flower
    ]

    mixed: list[QColor] = [
        QColor(33, 33, 33),  # Dark Grey
        QColor(50, 50, 50),  # Dark Anthracite
        QColor(245, 245, 245),  # Light Grey
        QColor(255, 255, 255),  # white
        QColor(0, 0, 0),  # Black
        QColor(105, 105, 105),  # Dim Gray
        QColor(169, 169, 169),  # Dark Gray
        QColor(211, 211, 211),  # Light Gray
        QColor(0, 0, 139),  # Dark Blue
        QColor(25, 25, 112),  # Midnight Blue
    ]
