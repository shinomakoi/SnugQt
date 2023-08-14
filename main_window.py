# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 1152)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionInpaint = QAction(MainWindow)
        self.actionInpaint.setObjectName(u"actionInpaint")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.previousImgButton = QPushButton(self.centralwidget)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 3, 2, 1, 1)

        self.negPromptLine = QPlainTextEdit(self.centralwidget)
        self.negPromptLine.setObjectName(u"negPromptLine")

        self.gridLayout.addWidget(self.negPromptLine, 3, 1, 2, 1)

        self.imgLabel = QGraphicsView(self.centralwidget)
        self.imgLabel.setObjectName(u"imgLabel")

        self.gridLayout.addWidget(self.imgLabel, 1, 0, 1, 4)

        self.nextImgButton = QPushButton(self.centralwidget)
        self.nextImgButton.setObjectName(u"nextImgButton")

        self.gridLayout.addWidget(self.nextImgButton, 3, 3, 1, 1)

        self.imgDisplayIndex = QLabel(self.centralwidget)
        self.imgDisplayIndex.setObjectName(u"imgDisplayIndex")

        self.gridLayout.addWidget(self.imgDisplayIndex, 2, 2, 1, 2, Qt.AlignHCenter)

        self.negPromptHistoryCombo = QComboBox(self.centralwidget)
        self.negPromptHistoryCombo.setObjectName(u"negPromptHistoryCombo")

        self.gridLayout.addWidget(self.negPromptHistoryCombo, 2, 1, 1, 1)

        self.promptLine = QPlainTextEdit(self.centralwidget)
        self.promptLine.setObjectName(u"promptLine")

        self.gridLayout.addWidget(self.promptLine, 3, 0, 2, 1)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setBold(True)
        self.generateButton.setFont(font)

        self.gridLayout.addWidget(self.generateButton, 4, 2, 1, 2)

        self.promptHistoryCombo = QComboBox(self.centralwidget)
        self.promptHistoryCombo.setObjectName(u"promptHistoryCombo")

        self.gridLayout.addWidget(self.promptHistoryCombo, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hiresFixCheck = QCheckBox(self.tab_3)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.horizontalLayout_3.addWidget(self.hiresFixCheck)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.tab_3)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(4.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.050000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.horizontalLayout_3.addWidget(self.hiresfixScaleByValue)

        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13, 0, Qt.AlignRight)

        self.hiresfixStepsValue = QSpinBox(self.tab_3)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(256)
        self.hiresfixStepsValue.setValue(12)

        self.horizontalLayout_3.addWidget(self.hiresfixStepsValue)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.hiresfixDenoiseSpin = QDoubleSpinBox(self.tab_3)
        self.hiresfixDenoiseSpin.setObjectName(u"hiresfixDenoiseSpin")
        self.hiresfixDenoiseSpin.setMaximum(1.000000000000000)
        self.hiresfixDenoiseSpin.setSingleStep(0.050000000000000)
        self.hiresfixDenoiseSpin.setValue(0.600000000000000)

        self.horizontalLayout_3.addWidget(self.hiresfixDenoiseSpin)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_28 = QLabel(self.tab_5)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_2.addWidget(self.label_28)

        self.img2imgLoadCombo = QComboBox(self.tab_5)
        self.img2imgLoadCombo.setObjectName(u"img2imgLoadCombo")

        self.horizontalLayout_2.addWidget(self.img2imgLoadCombo)

        self.img2imgLoadButton = QToolButton(self.tab_5)
        self.img2imgLoadButton.setObjectName(u"img2imgLoadButton")
        self.img2imgLoadButton.setArrowType(Qt.RightArrow)

        self.horizontalLayout_2.addWidget(self.img2imgLoadButton)

        self.label_29 = QLabel(self.tab_5)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_2.addWidget(self.label_29, 0, Qt.AlignRight)

        self.img2imgDenoiseSpin = QDoubleSpinBox(self.tab_5)
        self.img2imgDenoiseSpin.setObjectName(u"img2imgDenoiseSpin")
        self.img2imgDenoiseSpin.setMaximum(1.000000000000000)
        self.img2imgDenoiseSpin.setSingleStep(0.050000000000000)
        self.img2imgDenoiseSpin.setValue(0.700000000000000)

        self.horizontalLayout_2.addWidget(self.img2imgDenoiseSpin)

        self.line = QFrame(self.tab_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout = QHBoxLayout(self.tab_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_27 = QLabel(self.tab_4)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout.addWidget(self.label_27)

        self.inpaintLoadCombo = QComboBox(self.tab_4)
        self.inpaintLoadCombo.setObjectName(u"inpaintLoadCombo")

        self.horizontalLayout.addWidget(self.inpaintLoadCombo)

        self.inpaintLoadButton = QToolButton(self.tab_4)
        self.inpaintLoadButton.setObjectName(u"inpaintLoadButton")
        self.inpaintLoadButton.setArrowType(Qt.RightArrow)

        self.horizontalLayout.addWidget(self.inpaintLoadButton)

        self.label_26 = QLabel(self.tab_4)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout.addWidget(self.label_26, 0, Qt.AlignRight)

        self.inpaintDenoiseSpin = QDoubleSpinBox(self.tab_4)
        self.inpaintDenoiseSpin.setObjectName(u"inpaintDenoiseSpin")
        self.inpaintDenoiseSpin.setMaximum(1.000000000000000)
        self.inpaintDenoiseSpin.setSingleStep(0.050000000000000)
        self.inpaintDenoiseSpin.setValue(0.900000000000000)

        self.horizontalLayout.addWidget(self.inpaintDenoiseSpin)

        self.inpaintMaskEditorButton = QPushButton(self.tab_4)
        self.inpaintMaskEditorButton.setObjectName(u"inpaintMaskEditorButton")

        self.horizontalLayout.addWidget(self.inpaintMaskEditorButton)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 4, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 27))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.promptHistoryCombo, self.negPromptHistoryCombo)
        QWidget.setTabOrder(self.negPromptHistoryCombo, self.promptLine)
        QWidget.setTabOrder(self.promptLine, self.negPromptLine)
        QWidget.setTabOrder(self.negPromptLine, self.previousImgButton)
        QWidget.setTabOrder(self.previousImgButton, self.nextImgButton)
        QWidget.setTabOrder(self.nextImgButton, self.generateButton)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SnugQt", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionInpaint.setText(QCoreApplication.translate("MainWindow", u"Inpaint", None))
#if QT_CONFIG(tooltip)
        self.previousImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous image", None))
#endif // QT_CONFIG(tooltip)
        self.previousImgButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.negPromptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter negative prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.negPromptLine.setPlainText(QCoreApplication.translate("MainWindow", u"ugly, bad quality, worst quality, frame, text, watermark", None))
        self.negPromptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Negative prompt", None))
#if QT_CONFIG(tooltip)
        self.nextImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImgButton.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.nextImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.imgDisplayIndex.setToolTip(QCoreApplication.translate("MainWindow", u"Image index", None))
#endif // QT_CONFIG(tooltip)
        self.imgDisplayIndex.setText(QCoreApplication.translate("MainWindow", u"----", None))
#if QT_CONFIG(tooltip)
        self.negPromptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Negative prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.promptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.promptLine.setPlainText(QCoreApplication.translate("MainWindow", u"cute rabbit in the snow, photograph", None))
        self.promptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.promptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.hiresFixCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Enable hi-res fix", None))
#endif // QT_CONFIG(tooltip)
        self.hiresFixCheck.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upscale by:", None))
#if QT_CONFIG(tooltip)
        self.hiresfixScaleByValue.setToolTip(QCoreApplication.translate("MainWindow", u"Factor to scale hires-fix image by", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix steps:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Denoise:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Text to image", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
#if QT_CONFIG(tooltip)
        self.img2imgLoadCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Select image to use (from 'ComfyUI/input' folder)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.img2imgLoadButton.setToolTip(QCoreApplication.translate("MainWindow", u"Load images from 'ComfyUI/input' folder", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.img2imgDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Image to image", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
#if QT_CONFIG(tooltip)
        self.inpaintLoadCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Select image to use (from 'ComfyUI/input' folder)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inpaintLoadButton.setToolTip(QCoreApplication.translate("MainWindow", u"Load images from 'ComfyUI/input' folder", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.inpaintDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open editor to create a masked image for inpainting", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setText(QCoreApplication.translate("MainWindow", u"Inpaint mask editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

