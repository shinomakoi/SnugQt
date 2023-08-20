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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QToolBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1445, 1072)
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.promptHistoryCombo = QComboBox(self.centralwidget)
        self.promptHistoryCombo.setObjectName(u"promptHistoryCombo")

        self.gridLayout_2.addWidget(self.promptHistoryCombo, 1, 0, 1, 1)

        self.negPromptHistoryCombo = QComboBox(self.centralwidget)
        self.negPromptHistoryCombo.setObjectName(u"negPromptHistoryCombo")

        self.gridLayout_2.addWidget(self.negPromptHistoryCombo, 1, 1, 1, 1)

        self.imgDisplayIndex = QLabel(self.centralwidget)
        self.imgDisplayIndex.setObjectName(u"imgDisplayIndex")

        self.gridLayout_2.addWidget(self.imgDisplayIndex, 1, 2, 1, 2, Qt.AlignHCenter)

        self.promptLine = QPlainTextEdit(self.centralwidget)
        self.promptLine.setObjectName(u"promptLine")

        self.gridLayout_2.addWidget(self.promptLine, 2, 0, 2, 1)

        self.negPromptLine = QPlainTextEdit(self.centralwidget)
        self.negPromptLine.setObjectName(u"negPromptLine")

        self.gridLayout_2.addWidget(self.negPromptLine, 2, 1, 2, 1)

        self.previousImgButton = QPushButton(self.centralwidget)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout_2.addWidget(self.previousImgButton, 2, 2, 1, 1)

        self.nextImgButton = QPushButton(self.centralwidget)
        self.nextImgButton.setObjectName(u"nextImgButton")

        self.gridLayout_2.addWidget(self.nextImgButton, 2, 3, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(280, 16777215))
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QToolBox(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.txt2imgTab = QWidget()
        self.txt2imgTab.setObjectName(u"txt2imgTab")
        self.txt2imgTab.setGeometry(QRect(0, 0, 181, 676))
        self.gridLayout = QGridLayout(self.txt2imgTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hiresFixCheck = QCheckBox(self.txt2imgTab)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.gridLayout.addWidget(self.hiresFixCheck, 0, 0, 1, 1)

        self.label_13 = QLabel(self.txt2imgTab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.hiresfixDenoiseSpin = QDoubleSpinBox(self.txt2imgTab)
        self.hiresfixDenoiseSpin.setObjectName(u"hiresfixDenoiseSpin")
        self.hiresfixDenoiseSpin.setMaximum(1.000000000000000)
        self.hiresfixDenoiseSpin.setSingleStep(0.050000000000000)
        self.hiresfixDenoiseSpin.setValue(0.600000000000000)

        self.gridLayout.addWidget(self.hiresfixDenoiseSpin, 6, 0, 1, 1)

        self.label_2 = QLabel(self.txt2imgTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 479, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.label = QLabel(self.txt2imgTab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.hiresfixStepsValue = QSpinBox(self.txt2imgTab)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(256)
        self.hiresfixStepsValue.setValue(12)

        self.gridLayout.addWidget(self.hiresfixStepsValue, 4, 0, 1, 1)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.txt2imgTab)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(4.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.050000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.gridLayout.addWidget(self.hiresfixScaleByValue, 2, 0, 1, 1)

        self.tabWidget.addItem(self.txt2imgTab, u"Text to image")
        self.img2imgTab = QWidget()
        self.img2imgTab.setObjectName(u"img2imgTab")
        self.img2imgTab.setGeometry(QRect(0, 0, 179, 166))
        self.gridLayout_3 = QGridLayout(self.img2imgTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 2)

        self.label_29 = QLabel(self.img2imgTab)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_3 = QLabel(self.img2imgTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.img2imgLoadButton = QToolButton(self.img2imgTab)
        self.img2imgLoadButton.setObjectName(u"img2imgLoadButton")

        self.gridLayout_3.addWidget(self.img2imgLoadButton, 1, 1, 1, 1)

        self.img2imgLoadLine = QLineEdit(self.img2imgTab)
        self.img2imgLoadLine.setObjectName(u"img2imgLoadLine")

        self.gridLayout_3.addWidget(self.img2imgLoadLine, 1, 0, 1, 1)

        self.img2imgDenoiseSpin = QDoubleSpinBox(self.img2imgTab)
        self.img2imgDenoiseSpin.setObjectName(u"img2imgDenoiseSpin")
        self.img2imgDenoiseSpin.setMaximum(1.000000000000000)
        self.img2imgDenoiseSpin.setSingleStep(0.050000000000000)
        self.img2imgDenoiseSpin.setValue(0.700000000000000)

        self.gridLayout_3.addWidget(self.img2imgDenoiseSpin, 4, 0, 1, 2)

        self.tabWidget.addItem(self.img2imgTab, u"Image to image")
        self.inpaintTab = QWidget()
        self.inpaintTab.setObjectName(u"inpaintTab")
        self.inpaintTab.setGeometry(QRect(0, 0, 206, 305))
        self.gridLayout_4 = QGridLayout(self.inpaintTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.outpaintRSpin = QSpinBox(self.inpaintTab)
        self.outpaintRSpin.setObjectName(u"outpaintRSpin")
        self.outpaintRSpin.setMinimum(0)
        self.outpaintRSpin.setMaximum(1024)
        self.outpaintRSpin.setSingleStep(16)
        self.outpaintRSpin.setValue(128)

        self.gridLayout_4.addWidget(self.outpaintRSpin, 10, 1, 1, 1)

        self.label_4 = QLabel(self.inpaintTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 4, 1)

        self.outpaintUSpin = QSpinBox(self.inpaintTab)
        self.outpaintUSpin.setObjectName(u"outpaintUSpin")
        self.outpaintUSpin.setMinimum(0)
        self.outpaintUSpin.setMaximum(1024)
        self.outpaintUSpin.setSingleStep(16)
        self.outpaintUSpin.setValue(0)

        self.gridLayout_4.addWidget(self.outpaintUSpin, 12, 1, 1, 1)

        self.inpaintLoadButton = QToolButton(self.inpaintTab)
        self.inpaintLoadButton.setObjectName(u"inpaintLoadButton")

        self.gridLayout_4.addWidget(self.inpaintLoadButton, 4, 2, 1, 1)

        self.label_7 = QLabel(self.inpaintTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 10, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 14, 0, 1, 2)

        self.label_8 = QLabel(self.inpaintTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 11, 0, 1, 1)

        self.label_26 = QLabel(self.inpaintTab)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 5, 0, 1, 1)

        self.line_2 = QFrame(self.inpaintTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 8, 0, 1, 3)

        self.inpaintLoadLine = QLineEdit(self.inpaintTab)
        self.inpaintLoadLine.setObjectName(u"inpaintLoadLine")

        self.gridLayout_4.addWidget(self.inpaintLoadLine, 4, 0, 1, 2)

        self.label_9 = QLabel(self.inpaintTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 12, 0, 1, 1)

        self.outpaintDSpin = QSpinBox(self.inpaintTab)
        self.outpaintDSpin.setObjectName(u"outpaintDSpin")
        self.outpaintDSpin.setMinimum(0)
        self.outpaintDSpin.setMaximum(1024)
        self.outpaintDSpin.setSingleStep(16)
        self.outpaintDSpin.setValue(0)

        self.gridLayout_4.addWidget(self.outpaintDSpin, 13, 1, 1, 1)

        self.outpaintLSpin = QSpinBox(self.inpaintTab)
        self.outpaintLSpin.setObjectName(u"outpaintLSpin")
        self.outpaintLSpin.setMinimum(0)
        self.outpaintLSpin.setMaximum(1024)
        self.outpaintLSpin.setSingleStep(16)
        self.outpaintLSpin.setValue(0)

        self.gridLayout_4.addWidget(self.outpaintLSpin, 11, 1, 1, 1)

        self.label_10 = QLabel(self.inpaintTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 13, 0, 1, 1)

        self.outpaintCheck = QCheckBox(self.inpaintTab)
        self.outpaintCheck.setObjectName(u"outpaintCheck")

        self.gridLayout_4.addWidget(self.outpaintCheck, 9, 0, 1, 1)

        self.inpaintMaskEditorButton = QPushButton(self.inpaintTab)
        self.inpaintMaskEditorButton.setObjectName(u"inpaintMaskEditorButton")

        self.gridLayout_4.addWidget(self.inpaintMaskEditorButton, 7, 0, 1, 2)

        self.inpaintDenoiseSpin = QDoubleSpinBox(self.inpaintTab)
        self.inpaintDenoiseSpin.setObjectName(u"inpaintDenoiseSpin")
        self.inpaintDenoiseSpin.setMaximum(1.000000000000000)
        self.inpaintDenoiseSpin.setSingleStep(0.050000000000000)
        self.inpaintDenoiseSpin.setValue(0.900000000000000)

        self.gridLayout_4.addWidget(self.inpaintDenoiseSpin, 6, 0, 1, 2)

        self.tabWidget.addItem(self.inpaintTab, u"Inpainting")
        self.upscaleTab = QWidget()
        self.upscaleTab.setObjectName(u"upscaleTab")
        self.upscaleTab.setGeometry(QRect(0, 0, 181, 676))
        self.gridLayout_5 = QGridLayout(self.upscaleTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.upscaleLoadLine = QLineEdit(self.upscaleTab)
        self.upscaleLoadLine.setObjectName(u"upscaleLoadLine")

        self.gridLayout_5.addWidget(self.upscaleLoadLine, 1, 0, 1, 1)

        self.upscaleDownscaleCheck = QCheckBox(self.upscaleTab)
        self.upscaleDownscaleCheck.setObjectName(u"upscaleDownscaleCheck")

        self.gridLayout_5.addWidget(self.upscaleDownscaleCheck, 2, 0, 1, 1)

        self.label_5 = QLabel(self.upscaleTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.upscaleSpin = QSpinBox(self.upscaleTab)
        self.upscaleSpin.setObjectName(u"upscaleSpin")
        self.upscaleSpin.setMinimum(1)
        self.upscaleSpin.setValue(50)

        self.gridLayout_5.addWidget(self.upscaleSpin, 3, 0, 1, 2)

        self.upscaleLoadButton = QToolButton(self.upscaleTab)
        self.upscaleLoadButton.setObjectName(u"upscaleLoadButton")

        self.gridLayout_5.addWidget(self.upscaleLoadButton, 1, 1, 1, 1)

        self.tabWidget.addItem(self.upscaleTab, u"Upscale")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)

        self.promptStyleCombo = QComboBox(self.frame)
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.addItem("")
        self.promptStyleCombo.setObjectName(u"promptStyleCombo")
        self.promptStyleCombo.setMinimumSize(QSize(168, 0))

        self.gridLayout_6.addWidget(self.promptStyleCombo, 3, 0, 1, 1)

        self.splitter.addWidget(self.frame)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1221, 877))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.imageView = QLabel(self.scrollAreaWidgetContents_2)
        self.imageView.setObjectName(u"imageView")
        self.imageView.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.imageView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.splitter.addWidget(self.scrollArea)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 4)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setBold(True)
        self.generateButton.setFont(font)

        self.gridLayout_2.addWidget(self.generateButton, 3, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1445, 23))
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SnugQt", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionInpaint.setText(QCoreApplication.translate("MainWindow", u"Inpaint", None))
#if QT_CONFIG(tooltip)
        self.promptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.negPromptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Negative prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.imgDisplayIndex.setToolTip(QCoreApplication.translate("MainWindow", u"Image index", None))
#endif // QT_CONFIG(tooltip)
        self.imgDisplayIndex.setText(QCoreApplication.translate("MainWindow", u"----", None))
#if QT_CONFIG(tooltip)
        self.promptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.promptLine.setPlainText(QCoreApplication.translate("MainWindow", u"cute rabbit in the snow, photograph", None))
        self.promptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt", None))
#if QT_CONFIG(tooltip)
        self.negPromptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter negative prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.negPromptLine.setPlainText(QCoreApplication.translate("MainWindow", u"ugly, bad quality, worst quality, frame, text, watermark", None))
        self.negPromptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Negative prompt", None))
#if QT_CONFIG(tooltip)
        self.previousImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous image", None))
#endif // QT_CONFIG(tooltip)
        self.previousImgButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.nextImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImgButton.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.nextImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.hiresFixCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Enable hi-res fix", None))
#endif // QT_CONFIG(tooltip)
        self.hiresFixCheck.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix steps:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upscale by:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Denoise:", None))
#if QT_CONFIG(tooltip)
        self.hiresfixScaleByValue.setToolTip(QCoreApplication.translate("MainWindow", u"Factor to scale hires-fix image by", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.txt2imgTab), QCoreApplication.translate("MainWindow", u"Text to image", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.img2imgLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.img2imgDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.img2imgTab), QCoreApplication.translate("MainWindow", u"Image to image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.inpaintLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Left:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Up:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Down:", None))
        self.outpaintCheck.setText(QCoreApplication.translate("MainWindow", u"Outpaint", None))
#if QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open editor to create a masked image for inpainting", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setText(QCoreApplication.translate("MainWindow", u"Inpaint mask editor", None))
#if QT_CONFIG(tooltip)
        self.inpaintDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.inpaintTab), QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.upscaleDownscaleCheck.setText(QCoreApplication.translate("MainWindow", u"Downscale to:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.upscaleSpin.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.upscaleLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.upscaleTab), QCoreApplication.translate("MainWindow", u"Upscale", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Style:", None))
        self.promptStyleCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.promptStyleCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Enhance", None))
        self.promptStyleCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Anime", None))
        self.promptStyleCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Photographic", None))
        self.promptStyleCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"Digital art", None))
        self.promptStyleCombo.setItemText(5, QCoreApplication.translate("MainWindow", u"Fantasy art", None))
        self.promptStyleCombo.setItemText(6, QCoreApplication.translate("MainWindow", u"Analog film", None))
        self.promptStyleCombo.setItemText(7, QCoreApplication.translate("MainWindow", u"Line art", None))
        self.promptStyleCombo.setItemText(8, QCoreApplication.translate("MainWindow", u"Cinematic", None))
        self.promptStyleCombo.setItemText(9, QCoreApplication.translate("MainWindow", u"3D Model", None))
        self.promptStyleCombo.setItemText(10, QCoreApplication.translate("MainWindow", u"Pixel art", None))

#if QT_CONFIG(tooltip)
        self.promptStyleCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Apply style to prompt. Negative prompt is overridden", None))
#endif // QT_CONFIG(tooltip)
        self.imageView.setText(QCoreApplication.translate("MainWindow", u"Image display", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

