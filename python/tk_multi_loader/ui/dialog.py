# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1243, 754)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.toolbar_1 = QtGui.QHBoxLayout()
        self.toolbar_1.setObjectName("toolbar_1")
        self.navigation_home = QtGui.QToolButton(Dialog)
        self.navigation_home.setMinimumSize(QtCore.QSize(40, 40))
        self.navigation_home.setMaximumSize(QtCore.QSize(40, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navigation_home.setIcon(icon)
        self.navigation_home.setAutoRaise(True)
        self.navigation_home.setObjectName("navigation_home")
        self.toolbar_1.addWidget(self.navigation_home)
        self.navigation_prev = QtGui.QToolButton(Dialog)
        self.navigation_prev.setMinimumSize(QtCore.QSize(40, 40))
        self.navigation_prev.setMaximumSize(QtCore.QSize(40, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/arrow_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navigation_prev.setIcon(icon1)
        self.navigation_prev.setAutoRaise(True)
        self.navigation_prev.setObjectName("navigation_prev")
        self.toolbar_1.addWidget(self.navigation_prev)
        self.navigation_next = QtGui.QToolButton(Dialog)
        self.navigation_next.setMinimumSize(QtCore.QSize(40, 40))
        self.navigation_next.setMaximumSize(QtCore.QSize(40, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/arrow_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.navigation_next.setIcon(icon2)
        self.navigation_next.setAutoRaise(True)
        self.navigation_next.setObjectName("navigation_next")
        self.toolbar_1.addWidget(self.navigation_next)
        self.entity_breadcrumbs = QtGui.QLabel(Dialog)
        self.entity_breadcrumbs.setObjectName("entity_breadcrumbs")
        self.toolbar_1.addWidget(self.entity_breadcrumbs)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.toolbar_1.addItem(spacerItem)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.toolbar_1.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.toolbar_1, 0, 0, 1, 3)
        self.toolbar_2 = QtGui.QHBoxLayout()
        self.toolbar_2.setObjectName("toolbar_2")
        self.entity_button_layout = QtGui.QHBoxLayout()
        self.entity_button_layout.setObjectName("entity_button_layout")
        self.toolbar_2.addLayout(self.entity_button_layout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(68, 26, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.info = QtGui.QToolButton(Dialog)
        self.info.setCheckable(True)
        self.info.setObjectName("info")
        self.horizontalLayout_2.addWidget(self.info)
        self.toolbar_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.toolbar_2, 1, 0, 1, 3)
        self.middle_area = QtGui.QVBoxLayout()
        self.middle_area.setObjectName("middle_area")
        self.publish_grp = QtGui.QStackedWidget(Dialog)
        self.publish_grp.setObjectName("publish_grp")
        self.publish_list_page = QtGui.QWidget()
        self.publish_list_page.setObjectName("publish_list_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.publish_list_page)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.publish_list = QtGui.QListView(self.publish_list_page)
        self.publish_list.setStyleSheet("")
        self.publish_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.publish_list.setMovement(QtGui.QListView.Static)
        self.publish_list.setResizeMode(QtGui.QListView.Adjust)
        self.publish_list.setLayoutMode(QtGui.QListView.Batched)
        self.publish_list.setViewMode(QtGui.QListView.IconMode)
        self.publish_list.setUniformItemSizes(True)
        self.publish_list.setWordWrap(True)
        self.publish_list.setObjectName("publish_list")
        self.verticalLayout_5.addWidget(self.publish_list)
        self.publish_grp.addWidget(self.publish_list_page)
        self.publish_msg_page = QtGui.QWidget()
        self.publish_msg_page.setObjectName("publish_msg_page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.publish_msg_page)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.publish_msg = QtGui.QLabel(self.publish_msg_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publish_msg.sizePolicy().hasHeightForWidth())
        self.publish_msg.setSizePolicy(sizePolicy)
        self.publish_msg.setStyleSheet("QLabel { border: 1px solid black; }\n"
"\n"
"\n"
"")
        self.publish_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.publish_msg.setWordWrap(True)
        self.publish_msg.setObjectName("publish_msg")
        self.verticalLayout_3.addWidget(self.publish_msg)
        self.publish_grp.addWidget(self.publish_msg_page)
        self.middle_area.addWidget(self.publish_grp)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.global_progress = QtGui.QLabel(Dialog)
        self.global_progress.setText("")
        self.global_progress.setPixmap(QtGui.QPixmap(":/res/progress_bar_1.png"))
        self.global_progress.setObjectName("global_progress")
        self.horizontalLayout_4.addWidget(self.global_progress)
        spacerItem2 = QtGui.QSpacerItem(128, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.thumb_scale = QtGui.QSlider(Dialog)
        self.thumb_scale.setMinimumSize(QtCore.QSize(100, 0))
        self.thumb_scale.setMaximumSize(QtCore.QSize(100, 16777215))
        self.thumb_scale.setStyleSheet("QSlider::groove:horizontal {\n"
"     /*border: 1px solid #999999; */\n"
"     height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #3F3F3F, stop:1 #545454);\n"
"     margin: 2px 0;\n"
"     border-radius: 1px;\n"
" }\n"
"\n"
" QSlider::handle:horizontal {\n"
"     background: #545454;\n"
"     border: 1px solid #B6B6B6;\n"
"     width: 5px;\n"
"     margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 3px;\n"
" }\n"
"")
        self.thumb_scale.setMinimum(50)
        self.thumb_scale.setMaximum(300)
        self.thumb_scale.setProperty("value", 100)
        self.thumb_scale.setOrientation(QtCore.Qt.Horizontal)
        self.thumb_scale.setInvertedAppearance(False)
        self.thumb_scale.setInvertedControls(False)
        self.thumb_scale.setObjectName("thumb_scale")
        self.horizontalLayout_4.addWidget(self.thumb_scale)
        self.middle_area.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.middle_area, 2, 1, 1, 1)
        self.details = QtGui.QGroupBox(Dialog)
        self.details.setMinimumSize(QtCore.QSize(300, 0))
        self.details.setMaximumSize(QtCore.QSize(300, 16777215))
        self.details.setTitle("")
        self.details.setObjectName("details")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.details)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.details_grp = QtGui.QStackedWidget(self.details)
        self.details_grp.setObjectName("details_grp")
        self.details_list_page = QtGui.QWidget()
        self.details_list_page.setObjectName("details_list_page")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.details_list_page)
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.details_list = QtGui.QListView(self.details_list_page)
        self.details_list.setObjectName("details_list")
        self.verticalLayout_8.addWidget(self.details_list)
        self.details_grp.addWidget(self.details_list_page)
        self.details_msg_page = QtGui.QWidget()
        self.details_msg_page.setObjectName("details_msg_page")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.details_msg_page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.details_msg = QtGui.QLabel(self.details_msg_page)
        self.details_msg.setText("")
        self.details_msg.setPixmap(QtGui.QPixmap(":/res/progress_bar_1.png"))
        self.details_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.details_msg.setObjectName("details_msg")
        self.verticalLayout_9.addWidget(self.details_msg)
        self.details_grp.addWidget(self.details_msg_page)
        self.verticalLayout_4.addWidget(self.details_grp)
        self.gridLayout.addWidget(self.details, 2, 2, 1, 1)
        self.left_side_splitter = QtGui.QSplitter(Dialog)
        self.left_side_splitter.setOrientation(QtCore.Qt.Vertical)
        self.left_side_splitter.setObjectName("left_side_splitter")
        self.layoutWidget = QtGui.QWidget(self.left_side_splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.entity_grp = QtGui.QStackedWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_grp.sizePolicy().hasHeightForWidth())
        self.entity_grp.setSizePolicy(sizePolicy)
        self.entity_grp.setMinimumSize(QtCore.QSize(0, 400))
        self.entity_grp.setObjectName("entity_grp")
        self.entity_msg_page = QtGui.QWidget()
        self.entity_msg_page.setObjectName("entity_msg_page")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.entity_msg_page)
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.entity_msg = QtGui.QLabel(self.entity_msg_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_msg.sizePolicy().hasHeightForWidth())
        self.entity_msg.setSizePolicy(sizePolicy)
        self.entity_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_msg.setWordWrap(True)
        self.entity_msg.setObjectName("entity_msg")
        self.verticalLayout_11.addWidget(self.entity_msg)
        self.entity_grp.addWidget(self.entity_msg_page)
        self.verticalLayout.addWidget(self.entity_grp)
        self.layoutWidget1 = QtGui.QWidget(self.left_side_splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.publish_type_grp = QtGui.QStackedWidget(self.layoutWidget1)
        self.publish_type_grp.setObjectName("publish_type_grp")
        self.publish_type_list_page = QtGui.QWidget()
        self.publish_type_list_page.setObjectName("publish_type_list_page")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.publish_type_list_page)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.publish_type_list = QtGui.QListView(self.publish_type_list_page)
        self.publish_type_list.setMinimumSize(QtCore.QSize(0, 100))
        self.publish_type_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.publish_type_list.setProperty("showDropIndicator", False)
        self.publish_type_list.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.publish_type_list.setUniformItemSizes(True)
        self.publish_type_list.setObjectName("publish_type_list")
        self.verticalLayout_6.addWidget(self.publish_type_list)
        self.publish_type_grp.addWidget(self.publish_type_list_page)
        self.publish_type_msg_page = QtGui.QWidget()
        self.publish_type_msg_page.setObjectName("publish_type_msg_page")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.publish_type_msg_page)
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.publish_type_msg = QtGui.QLabel(self.publish_type_msg_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.publish_type_msg.sizePolicy().hasHeightForWidth())
        self.publish_type_msg.setSizePolicy(sizePolicy)
        self.publish_type_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.publish_type_msg.setWordWrap(True)
        self.publish_type_msg.setObjectName("publish_type_msg")
        self.verticalLayout_10.addWidget(self.publish_type_msg)
        self.publish_type_grp.addWidget(self.publish_type_msg_page)
        self.verticalLayout_2.addWidget(self.publish_type_grp)
        self.gridLayout.addWidget(self.left_side_splitter, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.publish_grp.setCurrentIndex(1)
        self.details_grp.setCurrentIndex(1)
        self.entity_grp.setCurrentIndex(0)
        self.publish_type_grp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Load items into your scene", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_home.setText(QtGui.QApplication.translate("Dialog", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_prev.setText(QtGui.QApplication.translate("Dialog", "< Back", None, QtGui.QApplication.UnicodeUTF8))
        self.navigation_next.setText(QtGui.QApplication.translate("Dialog", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_breadcrumbs.setText(QtGui.QApplication.translate("Dialog", "Breadcrumbs > Breadcrumbs > Breadcrumbs", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Dialog", "Search....", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "View Files from Sub Folders", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dialog", "Sort", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.info.setText(QtGui.QApplication.translate("Dialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_msg.setText(QtGui.QApplication.translate("Dialog", "Status messages from the Publish Model will show up this this part of the UI.", None, QtGui.QApplication.UnicodeUTF8))
        self.thumb_scale.setToolTip(QtGui.QApplication.translate("Dialog", "Thumbnail Size", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_msg.setText(QtGui.QApplication.translate("Dialog", "Status messages coming from the Entity listing tree views will show up here.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_type_msg.setText(QtGui.QApplication.translate("Dialog", "Status messages coming from the entity type listing model will show up here.", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
