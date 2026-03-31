# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QSize(1100, 700))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	font-size: 18px;\n"
"    font-family: 'JetBrains Mono';\n"
"}\n"
"\n"
"#sidebar QPushButton,\n"
"#media_page_header QPushButton,\n"
"#locked_folder_page_header QPushButton,\n"
"#photo_page_header QPushButton,\n"
"#video_page_header QPushButton,\n"
"#settings_page_scroll_area_widget QPushButton {\n"
"	border: none;\n"
"    border-radius: 25px;\n"
"    color: #444746;\n"
"    padding: 15px;\n"
"    text-align: left;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#sidebar QPushButton:hover,\n"
"#media_page_header QPushButton:hover,\n"
"#locked_folder_page_header QPushButton:hover,\n"
"#photo_page_header QPushButton:hover,\n"
"#video_page_header QPushButton:hover,\n"
"#settings_page_scroll_area_widget QPushButton:hover {\n"
"	background-color: #e5e5e5;\n"
"}\n"
"\n"
"#sidebar QPushButton:pressed,\n"
"#media_page_header QPushButton:pressed,\n"
"#locked_folder_page_header QPushButton:pressed,\n"
"#photo_page_header QPushButton:pressed,\n"
"#video_page_header QPushButton:pressed,\n"
"#settings_page_scroll_ar"
                        "ea_widget QPushButton:pressed {\n"
"	background-color: #c2ffc2;\n"
"}\n"
"\n"
"#widget_8 QPushButton {\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#widget_8 QPushButton:hover {\n"
"	background-color: #e5e5e5;\n"
"}\n"
"\n"
"#widget_8 QPushButton:pressed {\n"
"	background-color: #c2ffc2;\n"
"}\n"
"\n"
"#media_page_header_label, #locked_folder_page_header_label, #photo_page_header_label, #video_page_header_label, #settings_page_header_label {\n"
"	font-size: 22px;\n"
"}\n"
"\n"
"#settings_page_properties_main_label, #label, #label_4 {\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background: rgba(0, 0, 0, 0.1);\n"
"	width: 10px;\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background-color: #c2ffc2;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"	height: 0px;\n"
""
                        "}\n"
"\n"
"QComboBox, QFontComboBox {\n"
"	background-color: #f3f3f3;\n"
"	padding: 10px;\n"
"	border-radius: 15px;\n"
"}\n"
"            \n"
"QComboBox:hover, QFontComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}\n"
"            \n"
"QComboBox QAbstractItemView {\n"
"	background-color: #f3f3f3;\n"
"	selection-background-color: #c2ffc2;\n"
"	selection-color: #121212;\n"
"}\n"
"            \n"
"QComboBox QAbstractItemView::item {\n"
"	color: #444746;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_scroll_area = QScrollArea(self.centralwidget)
        self.sidebar_scroll_area.setObjectName(u"sidebar_scroll_area")
        self.sidebar_scroll_area.setMinimumSize(QSize(250, 0))
        self.sidebar_scroll_area.setMaximumSize(QSize(250, 16777215))
        self.sidebar_scroll_area.setStyleSheet(u"border: none;")
        self.sidebar_scroll_area.setWidgetResizable(True)
        self.sidebar = QWidget()
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 250, 682))
        self.sidebar.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.media_page_btn = QPushButton(self.sidebar)
        self.media_page_btn.setObjectName(u"media_page_btn")
        self.media_page_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/perm_media_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.media_page_btn.setIcon(icon)
        self.media_page_btn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.media_page_btn)

        self.photo_page_btn = QPushButton(self.sidebar)
        self.photo_page_btn.setObjectName(u"photo_page_btn")
        self.photo_page_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/photo_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.photo_page_btn.setIcon(icon1)
        self.photo_page_btn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.photo_page_btn)

        self.video_page_btn = QPushButton(self.sidebar)
        self.video_page_btn.setObjectName(u"video_page_btn")
        self.video_page_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/video_camera_back_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.video_page_btn.setIcon(icon2)
        self.video_page_btn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.video_page_btn)

        self.locked_folder_page_btn = QPushButton(self.sidebar)
        self.locked_folder_page_btn.setObjectName(u"locked_folder_page_btn")
        self.locked_folder_page_btn.setEnabled(True)
        self.locked_folder_page_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/lock_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.locked_folder_page_btn.setIcon(icon3)
        self.locked_folder_page_btn.setIconSize(QSize(24, 24))
        self.locked_folder_page_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.locked_folder_page_btn)

        self.settings_page_btn = QPushButton(self.sidebar)
        self.settings_page_btn.setObjectName(u"settings_page_btn")
        self.settings_page_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings_24dp_444746.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_page_btn.setIcon(icon4)
        self.settings_page_btn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.settings_page_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.sidebar_scroll_area.setWidget(self.sidebar)

        self.horizontalLayout.addWidget(self.sidebar_scroll_area)

        self.all_pages_stacked_widget = QStackedWidget(self.centralwidget)
        self.all_pages_stacked_widget.setObjectName(u"all_pages_stacked_widget")
        self.all_pages_stacked_widget.setStyleSheet(u"border: none;")
        self.media_page = QWidget()
        self.media_page.setObjectName(u"media_page")
        self.media_page.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.media_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.media_page_header = QWidget(self.media_page)
        self.media_page_header.setObjectName(u"media_page_header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.media_page_header.sizePolicy().hasHeightForWidth())
        self.media_page_header.setSizePolicy(sizePolicy)
        self.media_page_header.setMinimumSize(QSize(0, 0))
        self.media_page_header.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.media_page_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.media_page_header_label = QLabel(self.media_page_header)
        self.media_page_header_label.setObjectName(u"media_page_header_label")
        self.media_page_header_label.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.media_page_header_label)

        self.media_page_header_sort_files_btn = QPushButton(self.media_page_header)
        self.media_page_header_sort_files_btn.setObjectName(u"media_page_header_sort_files_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.media_page_header_sort_files_btn.sizePolicy().hasHeightForWidth())
        self.media_page_header_sort_files_btn.setSizePolicy(sizePolicy1)
        self.media_page_header_sort_files_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.media_page_header_sort_files_btn)

        self.media_page_header_back_to_files_area_btn = QPushButton(self.media_page_header)
        self.media_page_header_back_to_files_area_btn.setObjectName(u"media_page_header_back_to_files_area_btn")
        sizePolicy1.setHeightForWidth(self.media_page_header_back_to_files_area_btn.sizePolicy().hasHeightForWidth())
        self.media_page_header_back_to_files_area_btn.setSizePolicy(sizePolicy1)
        self.media_page_header_back_to_files_area_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.media_page_header_back_to_files_area_btn)

        self.media_page_header_create_album_btn = QPushButton(self.media_page_header)
        self.media_page_header_create_album_btn.setObjectName(u"media_page_header_create_album_btn")
        sizePolicy1.setHeightForWidth(self.media_page_header_create_album_btn.sizePolicy().hasHeightForWidth())
        self.media_page_header_create_album_btn.setSizePolicy(sizePolicy1)
        self.media_page_header_create_album_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.media_page_header_create_album_btn)

        self.media_page_header_add_files_btn = QPushButton(self.media_page_header)
        self.media_page_header_add_files_btn.setObjectName(u"media_page_header_add_files_btn")
        sizePolicy1.setHeightForWidth(self.media_page_header_add_files_btn.sizePolicy().hasHeightForWidth())
        self.media_page_header_add_files_btn.setSizePolicy(sizePolicy1)
        self.media_page_header_add_files_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.media_page_header_add_files_btn)


        self.verticalLayout_2.addWidget(self.media_page_header)

        self.media_page_page_scroll_area = QScrollArea(self.media_page)
        self.media_page_page_scroll_area.setObjectName(u"media_page_page_scroll_area")
        self.media_page_page_scroll_area.setMaximumSize(QSize(16777215, 16777215))
        self.media_page_page_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.media_page_page_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.media_page_page_scroll_area.setWidgetResizable(True)
        self.media_page_page_scroll_area_widget = QWidget()
        self.media_page_page_scroll_area_widget.setObjectName(u"media_page_page_scroll_area_widget")
        self.media_page_page_scroll_area_widget.setGeometry(QRect(0, 0, 90, 18))
        self.verticalLayout_3 = QVBoxLayout(self.media_page_page_scroll_area_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.media_page_files_area_stacked_widget = QStackedWidget(self.media_page_page_scroll_area_widget)
        self.media_page_files_area_stacked_widget.setObjectName(u"media_page_files_area_stacked_widget")
        self.media_page_files_area = QWidget()
        self.media_page_files_area.setObjectName(u"media_page_files_area")
        self.verticalLayout_4 = QVBoxLayout(self.media_page_files_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.media_page_files_area_stacked_widget.addWidget(self.media_page_files_area)
        self.media_page_files_area_2 = QWidget()
        self.media_page_files_area_2.setObjectName(u"media_page_files_area_2")
        self.verticalLayout_5 = QVBoxLayout(self.media_page_files_area_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.media_page_files_area_stacked_widget.addWidget(self.media_page_files_area_2)

        self.verticalLayout_3.addWidget(self.media_page_files_area_stacked_widget)

        self.media_page_page_scroll_area.setWidget(self.media_page_page_scroll_area_widget)

        self.verticalLayout_2.addWidget(self.media_page_page_scroll_area)

        self.all_pages_stacked_widget.addWidget(self.media_page)
        self.photo_page = QWidget()
        self.photo_page.setObjectName(u"photo_page")
        self.verticalLayout_10 = QVBoxLayout(self.photo_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.photo_page_header = QWidget(self.photo_page)
        self.photo_page_header.setObjectName(u"photo_page_header")
        self.horizontalLayout_4 = QHBoxLayout(self.photo_page_header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.photo_page_header_label = QLabel(self.photo_page_header)
        self.photo_page_header_label.setObjectName(u"photo_page_header_label")
        self.photo_page_header_label.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.photo_page_header_label)

        self.photo_page_header_sort_files_btn = QPushButton(self.photo_page_header)
        self.photo_page_header_sort_files_btn.setObjectName(u"photo_page_header_sort_files_btn")
        sizePolicy1.setHeightForWidth(self.photo_page_header_sort_files_btn.sizePolicy().hasHeightForWidth())
        self.photo_page_header_sort_files_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.photo_page_header_sort_files_btn)


        self.verticalLayout_10.addWidget(self.photo_page_header)

        self.photo_page_scroll_area = QScrollArea(self.photo_page)
        self.photo_page_scroll_area.setObjectName(u"photo_page_scroll_area")
        self.photo_page_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.photo_page_scroll_area.setWidgetResizable(True)
        self.photo_page_files_area = QWidget()
        self.photo_page_files_area.setObjectName(u"photo_page_files_area")
        self.photo_page_files_area.setGeometry(QRect(0, 0, 826, 624))
        self.verticalLayout_11 = QVBoxLayout(self.photo_page_files_area)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.photo_page_scroll_area.setWidget(self.photo_page_files_area)

        self.verticalLayout_10.addWidget(self.photo_page_scroll_area)

        self.all_pages_stacked_widget.addWidget(self.photo_page)
        self.video_page = QWidget()
        self.video_page.setObjectName(u"video_page")
        self.verticalLayout_12 = QVBoxLayout(self.video_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.video_page_header = QWidget(self.video_page)
        self.video_page_header.setObjectName(u"video_page_header")
        self.horizontalLayout_5 = QHBoxLayout(self.video_page_header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.video_page_header_label = QLabel(self.video_page_header)
        self.video_page_header_label.setObjectName(u"video_page_header_label")
        self.video_page_header_label.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.video_page_header_label)

        self.video_page_header_sort_files_btn = QPushButton(self.video_page_header)
        self.video_page_header_sort_files_btn.setObjectName(u"video_page_header_sort_files_btn")
        sizePolicy1.setHeightForWidth(self.video_page_header_sort_files_btn.sizePolicy().hasHeightForWidth())
        self.video_page_header_sort_files_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.video_page_header_sort_files_btn)


        self.verticalLayout_12.addWidget(self.video_page_header)

        self.video_page_scroll_area = QScrollArea(self.video_page)
        self.video_page_scroll_area.setObjectName(u"video_page_scroll_area")
        self.video_page_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.video_page_scroll_area.setWidgetResizable(True)
        self.video_page_files_area = QWidget()
        self.video_page_files_area.setObjectName(u"video_page_files_area")
        self.video_page_files_area.setGeometry(QRect(0, 0, 826, 624))
        self.verticalLayout_13 = QVBoxLayout(self.video_page_files_area)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_7 = QSpacerItem(20, 644, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_7)

        self.video_page_scroll_area.setWidget(self.video_page_files_area)

        self.verticalLayout_12.addWidget(self.video_page_scroll_area)

        self.all_pages_stacked_widget.addWidget(self.video_page)
        self.locked_folder_page = QWidget()
        self.locked_folder_page.setObjectName(u"locked_folder_page")
        self.verticalLayout_6 = QVBoxLayout(self.locked_folder_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.locked_folder_page_header = QWidget(self.locked_folder_page)
        self.locked_folder_page_header.setObjectName(u"locked_folder_page_header")
        self.horizontalLayout_3 = QHBoxLayout(self.locked_folder_page_header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.locked_folder_page_header_label = QLabel(self.locked_folder_page_header)
        self.locked_folder_page_header_label.setObjectName(u"locked_folder_page_header_label")
        self.locked_folder_page_header_label.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.locked_folder_page_header_label)

        self.locked_folder_page_header_sort_files_btn = QPushButton(self.locked_folder_page_header)
        self.locked_folder_page_header_sort_files_btn.setObjectName(u"locked_folder_page_header_sort_files_btn")
        sizePolicy1.setHeightForWidth(self.locked_folder_page_header_sort_files_btn.sizePolicy().hasHeightForWidth())
        self.locked_folder_page_header_sort_files_btn.setSizePolicy(sizePolicy1)
        self.locked_folder_page_header_sort_files_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.locked_folder_page_header_sort_files_btn)

        self.locked_folder_page_header_back_to_files_area_btn = QPushButton(self.locked_folder_page_header)
        self.locked_folder_page_header_back_to_files_area_btn.setObjectName(u"locked_folder_page_header_back_to_files_area_btn")
        sizePolicy1.setHeightForWidth(self.locked_folder_page_header_back_to_files_area_btn.sizePolicy().hasHeightForWidth())
        self.locked_folder_page_header_back_to_files_area_btn.setSizePolicy(sizePolicy1)
        self.locked_folder_page_header_back_to_files_area_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.locked_folder_page_header_back_to_files_area_btn)

        self.locked_folder_page_header_create_album_btn = QPushButton(self.locked_folder_page_header)
        self.locked_folder_page_header_create_album_btn.setObjectName(u"locked_folder_page_header_create_album_btn")
        sizePolicy1.setHeightForWidth(self.locked_folder_page_header_create_album_btn.sizePolicy().hasHeightForWidth())
        self.locked_folder_page_header_create_album_btn.setSizePolicy(sizePolicy1)
        self.locked_folder_page_header_create_album_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.locked_folder_page_header_create_album_btn)

        self.locked_folder_page_header_add_files_btn = QPushButton(self.locked_folder_page_header)
        self.locked_folder_page_header_add_files_btn.setObjectName(u"locked_folder_page_header_add_files_btn")
        sizePolicy1.setHeightForWidth(self.locked_folder_page_header_add_files_btn.sizePolicy().hasHeightForWidth())
        self.locked_folder_page_header_add_files_btn.setSizePolicy(sizePolicy1)
        self.locked_folder_page_header_add_files_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.locked_folder_page_header_add_files_btn)


        self.verticalLayout_6.addWidget(self.locked_folder_page_header)

        self.locked_folder_page_scroll_area = QScrollArea(self.locked_folder_page)
        self.locked_folder_page_scroll_area.setObjectName(u"locked_folder_page_scroll_area")
        self.locked_folder_page_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.locked_folder_page_scroll_area.setWidgetResizable(True)
        self.locked_folder_page_scroll_area_widget = QWidget()
        self.locked_folder_page_scroll_area_widget.setObjectName(u"locked_folder_page_scroll_area_widget")
        self.locked_folder_page_scroll_area_widget.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_8 = QVBoxLayout(self.locked_folder_page_scroll_area_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.locked_folder_page_files_area_stacked_widget = QStackedWidget(self.locked_folder_page_scroll_area_widget)
        self.locked_folder_page_files_area_stacked_widget.setObjectName(u"locked_folder_page_files_area_stacked_widget")
        self.locked_folder_page_files_area = QWidget()
        self.locked_folder_page_files_area.setObjectName(u"locked_folder_page_files_area")
        self.verticalLayout_7 = QVBoxLayout(self.locked_folder_page_files_area)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_4 = QSpacerItem(20, 602, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.locked_folder_page_files_area_stacked_widget.addWidget(self.locked_folder_page_files_area)
        self.locked_folder_page_files_area_2 = QWidget()
        self.locked_folder_page_files_area_2.setObjectName(u"locked_folder_page_files_area_2")
        self.verticalLayout_9 = QVBoxLayout(self.locked_folder_page_files_area_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_5 = QSpacerItem(20, 602, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_5)

        self.locked_folder_page_files_area_stacked_widget.addWidget(self.locked_folder_page_files_area_2)

        self.verticalLayout_8.addWidget(self.locked_folder_page_files_area_stacked_widget)

        self.locked_folder_page_scroll_area.setWidget(self.locked_folder_page_scroll_area_widget)

        self.verticalLayout_6.addWidget(self.locked_folder_page_scroll_area)

        self.all_pages_stacked_widget.addWidget(self.locked_folder_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_14 = QVBoxLayout(self.settings_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.settings_page_header = QWidget(self.settings_page)
        self.settings_page_header.setObjectName(u"settings_page_header")
        self.verticalLayout_15 = QVBoxLayout(self.settings_page_header)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.settings_page_header_label = QLabel(self.settings_page_header)
        self.settings_page_header_label.setObjectName(u"settings_page_header_label")

        self.verticalLayout_15.addWidget(self.settings_page_header_label)


        self.verticalLayout_14.addWidget(self.settings_page_header)

        self.settings_page_scroll_area = QScrollArea(self.settings_page)
        self.settings_page_scroll_area.setObjectName(u"settings_page_scroll_area")
        self.settings_page_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settings_page_scroll_area.setWidgetResizable(True)
        self.settings_page_scroll_area_widget = QWidget()
        self.settings_page_scroll_area_widget.setObjectName(u"settings_page_scroll_area_widget")
        self.settings_page_scroll_area_widget.setGeometry(QRect(0, 0, 816, 786))
        self.verticalLayout_16 = QVBoxLayout(self.settings_page_scroll_area_widget)
        self.verticalLayout_16.setSpacing(30)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.widget_9 = QWidget(self.settings_page_scroll_area_widget)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.verticalLayout_17.addWidget(self.label_8)

        self.widget = QWidget(self.widget_9)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_18 = QVBoxLayout(self.widget)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.settings_page_auto_preview = QCheckBox(self.widget)
        self.settings_page_auto_preview.setObjectName(u"settings_page_auto_preview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settings_page_auto_preview.sizePolicy().hasHeightForWidth())
        self.settings_page_auto_preview.setSizePolicy(sizePolicy2)
        self.settings_page_auto_preview.setChecked(True)

        self.verticalLayout_18.addWidget(self.settings_page_auto_preview)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.settings_page_def_folder_btn = QPushButton(self.widget_10)
        self.settings_page_def_folder_btn.setObjectName(u"settings_page_def_folder_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.settings_page_def_folder_btn.sizePolicy().hasHeightForWidth())
        self.settings_page_def_folder_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.settings_page_def_folder_btn)


        self.verticalLayout_18.addWidget(self.widget_10)

        self.settings_page_file_del_ask_check_box = QCheckBox(self.widget)
        self.settings_page_file_del_ask_check_box.setObjectName(u"settings_page_file_del_ask_check_box")
        sizePolicy2.setHeightForWidth(self.settings_page_file_del_ask_check_box.sizePolicy().hasHeightForWidth())
        self.settings_page_file_del_ask_check_box.setSizePolicy(sizePolicy2)

        self.verticalLayout_18.addWidget(self.settings_page_file_del_ask_check_box)

        self.settings_page_album_del_ask_check_box = QCheckBox(self.widget)
        self.settings_page_album_del_ask_check_box.setObjectName(u"settings_page_album_del_ask_check_box")
        sizePolicy2.setHeightForWidth(self.settings_page_album_del_ask_check_box.sizePolicy().hasHeightForWidth())
        self.settings_page_album_del_ask_check_box.setSizePolicy(sizePolicy2)
        self.settings_page_album_del_ask_check_box.setChecked(True)

        self.verticalLayout_18.addWidget(self.settings_page_album_del_ask_check_box)

        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_11)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.settings_page_open_data_file_btn = QPushButton(self.widget_11)
        self.settings_page_open_data_file_btn.setObjectName(u"settings_page_open_data_file_btn")
        sizePolicy3.setHeightForWidth(self.settings_page_open_data_file_btn.sizePolicy().hasHeightForWidth())
        self.settings_page_open_data_file_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.settings_page_open_data_file_btn)


        self.verticalLayout_18.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_12)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.settings_page_remove_data_btn = QPushButton(self.widget_12)
        self.settings_page_remove_data_btn.setObjectName(u"settings_page_remove_data_btn")
        sizePolicy3.setHeightForWidth(self.settings_page_remove_data_btn.sizePolicy().hasHeightForWidth())
        self.settings_page_remove_data_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.settings_page_remove_data_btn)


        self.verticalLayout_18.addWidget(self.widget_12)


        self.verticalLayout_17.addWidget(self.widget)


        self.verticalLayout_16.addWidget(self.widget_9)

        self.widget_2 = QWidget(self.settings_page_scroll_area_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_19 = QVBoxLayout(self.widget_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_19.addWidget(self.label)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_20 = QVBoxLayout(self.widget_3)
        self.verticalLayout_20.setSpacing(20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.settings_page_accent_color_combo_box = QComboBox(self.widget_4)
        self.settings_page_accent_color_combo_box.setObjectName(u"settings_page_accent_color_combo_box")

        self.horizontalLayout_6.addWidget(self.settings_page_accent_color_combo_box)


        self.verticalLayout_20.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.settings_page_font_combo_box = QFontComboBox(self.widget_5)
        self.settings_page_font_combo_box.setObjectName(u"settings_page_font_combo_box")

        self.horizontalLayout_7.addWidget(self.settings_page_font_combo_box)


        self.verticalLayout_20.addWidget(self.widget_5)


        self.verticalLayout_19.addWidget(self.widget_3)


        self.verticalLayout_16.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.settings_page_scroll_area_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_21 = QVBoxLayout(self.widget_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_21.addWidget(self.label_4)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_22 = QVBoxLayout(self.widget_7)
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_22.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_22.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_22.addWidget(self.label_7)


        self.verticalLayout_21.addWidget(self.widget_7)


        self.verticalLayout_16.addWidget(self.widget_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)

        self.settings_page_scroll_area.setWidget(self.settings_page_scroll_area_widget)

        self.verticalLayout_14.addWidget(self.settings_page_scroll_area)

        self.all_pages_stacked_widget.addWidget(self.settings_page)

        self.horizontalLayout.addWidget(self.all_pages_stacked_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.all_pages_stacked_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyGallery", None))
        self.media_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430", None))
        self.photo_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e", None))
        self.video_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.locked_folder_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u0430\u044f \u043f\u0430\u043f\u043a\u0430", None))
        self.settings_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.media_page_header_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430", None))
        self.media_page_header_sort_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.media_page_header_back_to_files_area_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.media_page_header_create_album_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043b\u044c\u0431\u043e\u043c", None))
        self.media_page_header_add_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.photo_page_header_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e", None))
        self.photo_page_header_sort_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.video_page_header_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e", None))
        self.video_page_header_sort_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.locked_folder_page_header_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430 (\u0441\u043a\u0440\u044b\u0442\u043e\u0435)", None))
        self.locked_folder_page_header_sort_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.locked_folder_page_header_back_to_files_area_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.locked_folder_page_header_create_album_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043b\u044c\u0431\u043e\u043c", None))
        self.locked_folder_page_header_add_files_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.settings_page_header_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.settings_page_auto_preview.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043f\u0440\u0435\u0432\u044c\u044e \u0434\u043b\u044f \u0444\u043e\u0442\u043e \u0438 \u0432\u0438\u0434\u0435\u043e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f \u043f\u0430\u043f\u043a\u0430 \u043f\u0440\u0438 \u0432\u044b\u0431\u043e\u0440\u0435 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.settings_page_def_folder_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.settings_page_file_del_ask_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0434 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435\u043c \u0444\u0430\u0439\u043b\u0430", None))
        self.settings_page_album_del_ask_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0434 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435\u043c \u0430\u043b\u044c\u0431\u043e\u043c\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.settings_page_open_data_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.settings_page_remove_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0438\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0446\u0435\u043d\u0442\u043d\u044b\u0439 \u0446\u0432\u0435\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f: 1.0.0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440: Loyalny", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Git Hub: https://github.com/loyalny", None))
    # retranslateUi

