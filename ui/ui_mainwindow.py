# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QToolButton, QVBoxLayout,
    QWidget)
from . import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 815)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/base_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_info = QToolButton(self.frame)
        self.toolButton_info.setObjectName(u"toolButton_info")
        font = QFont()
        font.setPointSize(11)
        self.toolButton_info.setFont(font)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        self.toolButton_info.setIcon(icon1)
        self.toolButton_info.setIconSize(QSize(23, 23))

        self.horizontalLayout.addWidget(self.toolButton_info)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.toolButton_path_reset = QToolButton(self.frame)
        self.toolButton_path_reset.setObjectName(u"toolButton_path_reset")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.toolButton_path_reset.setIcon(icon2)
        self.toolButton_path_reset.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.toolButton_path_reset)


        self.verticalLayout.addWidget(self.frame)

        self.listWidget_path = QListWidget(self.widget)
        self.listWidget_path.setObjectName(u"listWidget_path")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listWidget_path.sizePolicy().hasHeightForWidth())
        self.listWidget_path.setSizePolicy(sizePolicy4)
        self.listWidget_path.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.listWidget_path)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButton_path_add = QPushButton(self.frame_2)
        self.pushButton_path_add.setObjectName(u"pushButton_path_add")
        self.pushButton_path_add.setFont(font)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton_path_add.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton_path_add)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_path_remove = QPushButton(self.frame_2)
        self.pushButton_path_remove.setObjectName(u"pushButton_path_remove")
        self.pushButton_path_remove.setFont(font)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.pushButton_path_remove.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButton_path_remove)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.frame_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.widget_3 = QWidget(self.frame_5)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lcdNumber_duplicate_files = QLCDNumber(self.widget_3)
        self.lcdNumber_duplicate_files.setObjectName(u"lcdNumber_duplicate_files")
        sizePolicy3.setHeightForWidth(self.lcdNumber_duplicate_files.sizePolicy().hasHeightForWidth())
        self.lcdNumber_duplicate_files.setSizePolicy(sizePolicy3)
        self.lcdNumber_duplicate_files.setFont(font1)
        self.lcdNumber_duplicate_files.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_duplicate_files.setFrameShadow(QFrame.Shadow.Sunken)
        self.lcdNumber_duplicate_files.setLineWidth(1)
        self.lcdNumber_duplicate_files.setMidLineWidth(0)
        self.lcdNumber_duplicate_files.setDigitCount(14)
        self.lcdNumber_duplicate_files.setMode(QLCDNumber.Mode.Dec)
        self.lcdNumber_duplicate_files.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout_5.addWidget(self.lcdNumber_duplicate_files)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy5.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy5)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.pushButton_scan = QPushButton(self.widget_5)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setEnabled(True)
        self.pushButton_scan.setFont(font)
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemSearch))
        self.pushButton_scan.setIcon(icon5)
        self.pushButton_scan.setCheckable(False)

        self.horizontalLayout_7.addWidget(self.pushButton_scan)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.line_3 = QFrame(self.frame_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.groupBox_deleteOptions_time = QGroupBox(self.frame_5)
        self.groupBox_deleteOptions_time.setObjectName(u"groupBox_deleteOptions_time")
        sizePolicy3.setHeightForWidth(self.groupBox_deleteOptions_time.sizePolicy().hasHeightForWidth())
        self.groupBox_deleteOptions_time.setSizePolicy(sizePolicy3)
        self.groupBox_deleteOptions_time.setFont(font)
        self.groupBox_deleteOptions_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_deleteOptions_time)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_deleteOptions_time_new = QRadioButton(self.groupBox_deleteOptions_time)
        self.radioButton_deleteOptions_time_new.setObjectName(u"radioButton_deleteOptions_time_new")
        self.radioButton_deleteOptions_time_new.setFont(font)

        self.horizontalLayout_3.addWidget(self.radioButton_deleteOptions_time_new)

        self.radioButton_deleteOptions_time_old = QRadioButton(self.groupBox_deleteOptions_time)
        self.radioButton_deleteOptions_time_old.setObjectName(u"radioButton_deleteOptions_time_old")
        self.radioButton_deleteOptions_time_old.setFont(font)

        self.horizontalLayout_3.addWidget(self.radioButton_deleteOptions_time_old)


        self.verticalLayout_4.addWidget(self.groupBox_deleteOptions_time)

        self.widget_4 = QWidget(self.frame_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy5.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy5)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pushButton_deleteOptions_delete = QPushButton(self.widget_4)
        self.pushButton_deleteOptions_delete.setObjectName(u"pushButton_deleteOptions_delete")
        self.pushButton_deleteOptions_delete.setFont(font)
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButton_deleteOptions_delete.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.pushButton_deleteOptions_delete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.listWidget_delete_file_path = QListWidget(self.frame_5)
        self.listWidget_delete_file_path.setObjectName(u"listWidget_delete_file_path")
        sizePolicy3.setHeightForWidth(self.listWidget_delete_file_path.sizePolicy().hasHeightForWidth())
        self.listWidget_delete_file_path.setSizePolicy(sizePolicy3)
        self.listWidget_delete_file_path.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_4.addWidget(self.listWidget_delete_file_path)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.tableView_result = QTableView(self.centralwidget)
        self.tableView_result.setObjectName(u"tableView_result")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableView_result.sizePolicy().hasHeightForWidth())
        self.tableView_result.setSizePolicy(sizePolicy7)
        self.tableView_result.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_4.addWidget(self.tableView_result)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.progressBar_scan = QProgressBar(self.centralwidget)
        self.progressBar_scan.setObjectName(u"progressBar_scan")
        self.progressBar_scan.setMaximum(0)
        self.progressBar_scan.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar_scan)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 937, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DediDuplicator", None))
#if QT_CONFIG(tooltip)
        self.toolButton_info.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the application and the person who made the application.", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_info.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Places to look for duplicates", None))
#if QT_CONFIG(tooltip)
        self.toolButton_path_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Clears the search list.", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_path_reset.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_path_add.setToolTip(QCoreApplication.translate("MainWindow", u"Adds paths to search.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_path_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.pushButton_path_remove.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes the selected path from the search list.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_path_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of duplicate files :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_scan.setToolTip(QCoreApplication.translate("MainWindow", u"Finds duplicate files in added paths.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delete options", None))
        self.groupBox_deleteOptions_time.setTitle(QCoreApplication.translate("MainWindow", u"Creation Time", None))
#if QT_CONFIG(tooltip)
        self.radioButton_deleteOptions_time_new.setToolTip(QCoreApplication.translate("MainWindow", u"Chooses to delete new files", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_deleteOptions_time_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.radioButton_deleteOptions_time_old.setToolTip(QCoreApplication.translate("MainWindow", u"Chooses to delete old files", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_deleteOptions_time_old.setText(QCoreApplication.translate("MainWindow", u"Old", None))
#if QT_CONFIG(tooltip)
        self.pushButton_deleteOptions_delete.setToolTip(QCoreApplication.translate("MainWindow", u"Deletes files with the select column marked", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_deleteOptions_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Undeleted files", None))
    # retranslateUi

