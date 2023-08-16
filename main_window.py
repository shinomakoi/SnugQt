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
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QToolButton,
    QWidget)

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
        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setBold(True)
        self.generateButton.setFont(font)

        self.gridLayout.addWidget(self.generateButton, 4, 2, 1, 2)

        self.imgDisplayIndex = QLabel(self.centralwidget)
        self.imgDisplayIndex.setObjectName(u"imgDisplayIndex")

        self.gridLayout.addWidget(self.imgDisplayIndex, 2, 2, 1, 2, Qt.AlignHCenter)

        self.negPromptLine = QPlainTextEdit(self.centralwidget)
        self.negPromptLine.setObjectName(u"negPromptLine")

        self.gridLayout.addWidget(self.negPromptLine, 3, 1, 2, 1)

        self.promptHistoryCombo = QComboBox(self.centralwidget)
        self.promptHistoryCombo.setObjectName(u"promptHistoryCombo")

        self.gridLayout.addWidget(self.promptHistoryCombo, 2, 0, 1, 1)

        self.negPromptHistoryCombo = QComboBox(self.centralwidget)
        self.negPromptHistoryCombo.setObjectName(u"negPromptHistoryCombo")

        self.gridLayout.addWidget(self.negPromptHistoryCombo, 2, 1, 1, 1)

        self.imgLabel = QGraphicsView(self.centralwidget)
        self.imgLabel.setObjectName(u"imgLabel")

        self.gridLayout.addWidget(self.imgLabel, 1, 0, 1, 4)

        self.nextImgButton = QPushButton(self.centralwidget)
        self.nextImgButton.setObjectName(u"nextImgButton")

        self.gridLayout.addWidget(self.nextImgButton, 3, 3, 1, 1)

        self.previousImgButton = QPushButton(self.centralwidget)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 3, 2, 1, 1)

        self.promptLine = QPlainTextEdit(self.centralwidget)
        self.promptLine.setObjectName(u"promptLine")

        self.gridLayout.addWidget(self.promptLine, 3, 0, 2, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.txt2imgTab = QWidget()
        self.txt2imgTab.setObjectName(u"txt2imgTab")
        self.horizontalLayout_3 = QHBoxLayout(self.txt2imgTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hiresFixCheck = QCheckBox(self.txt2imgTab)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.horizontalLayout_3.addWidget(self.hiresFixCheck)

        self.label_2 = QLabel(self.txt2imgTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.txt2imgTab)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(4.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.050000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.horizontalLayout_3.addWidget(self.hiresfixScaleByValue)

        self.label_13 = QLabel(self.txt2imgTab)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.hiresfixStepsValue = QSpinBox(self.txt2imgTab)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(256)
        self.hiresfixStepsValue.setValue(12)

        self.horizontalLayout_3.addWidget(self.hiresfixStepsValue)

        self.label = QLabel(self.txt2imgTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.hiresfixDenoiseSpin = QDoubleSpinBox(self.txt2imgTab)
        self.hiresfixDenoiseSpin.setObjectName(u"hiresfixDenoiseSpin")
        self.hiresfixDenoiseSpin.setMaximum(1.000000000000000)
        self.hiresfixDenoiseSpin.setSingleStep(0.050000000000000)
        self.hiresfixDenoiseSpin.setValue(0.600000000000000)

        self.horizontalLayout_3.addWidget(self.hiresfixDenoiseSpin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.txt2imgTab, "")
        self.img2imgTab = QWidget()
        self.img2imgTab.setObjectName(u"img2imgTab")
        self.horizontalLayout_2 = QHBoxLayout(self.img2imgTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.img2imgTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.img2imgLoadLine = QLineEdit(self.img2imgTab)
        self.img2imgLoadLine.setObjectName(u"img2imgLoadLine")

        self.horizontalLayout_2.addWidget(self.img2imgLoadLine)

        self.img2imgLoadButton = QToolButton(self.img2imgTab)
        self.img2imgLoadButton.setObjectName(u"img2imgLoadButton")

        self.horizontalLayout_2.addWidget(self.img2imgLoadButton)

        self.label_29 = QLabel(self.img2imgTab)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_2.addWidget(self.label_29, 0, Qt.AlignRight)

        self.img2imgDenoiseSpin = QDoubleSpinBox(self.img2imgTab)
        self.img2imgDenoiseSpin.setObjectName(u"img2imgDenoiseSpin")
        self.img2imgDenoiseSpin.setMaximum(1.000000000000000)
        self.img2imgDenoiseSpin.setSingleStep(0.050000000000000)
        self.img2imgDenoiseSpin.setValue(0.700000000000000)

        self.horizontalLayout_2.addWidget(self.img2imgDenoiseSpin)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.tabWidget.addTab(self.img2imgTab, "")
        self.inpaintTab = QWidget()
        self.inpaintTab.setObjectName(u"inpaintTab")
        self.horizontalLayout = QHBoxLayout(self.inpaintTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.inpaintTab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.inpaintLoadLine = QLineEdit(self.inpaintTab)
        self.inpaintLoadLine.setObjectName(u"inpaintLoadLine")

        self.horizontalLayout.addWidget(self.inpaintLoadLine)

        self.inpaintLoadButton = QToolButton(self.inpaintTab)
        self.inpaintLoadButton.setObjectName(u"inpaintLoadButton")

        self.horizontalLayout.addWidget(self.inpaintLoadButton)

        self.label_26 = QLabel(self.inpaintTab)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout.addWidget(self.label_26, 0, Qt.AlignRight)

        self.inpaintDenoiseSpin = QDoubleSpinBox(self.inpaintTab)
        self.inpaintDenoiseSpin.setObjectName(u"inpaintDenoiseSpin")
        self.inpaintDenoiseSpin.setMaximum(1.000000000000000)
        self.inpaintDenoiseSpin.setSingleStep(0.050000000000000)
        self.inpaintDenoiseSpin.setValue(0.900000000000000)

        self.horizontalLayout.addWidget(self.inpaintDenoiseSpin)

        self.inpaintMaskEditorButton = QPushButton(self.inpaintTab)
        self.inpaintMaskEditorButton.setObjectName(u"inpaintMaskEditorButton")

        self.horizontalLayout.addWidget(self.inpaintMaskEditorButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.tabWidget.addTab(self.inpaintTab, "")
        self.upscaleTab = QWidget()
        self.upscaleTab.setObjectName(u"upscaleTab")
        self.horizontalLayout_4 = QHBoxLayout(self.upscaleTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.upscaleTab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.upscaleLoadLine = QLineEdit(self.upscaleTab)
        self.upscaleLoadLine.setObjectName(u"upscaleLoadLine")

        self.horizontalLayout_4.addWidget(self.upscaleLoadLine)

        self.upscaleLoadButton = QToolButton(self.upscaleTab)
        self.upscaleLoadButton.setObjectName(u"upscaleLoadButton")

        self.horizontalLayout_4.addWidget(self.upscaleLoadButton)

        self.upscaleDownscaleCheck = QCheckBox(self.upscaleTab)
        self.upscaleDownscaleCheck.setObjectName(u"upscaleDownscaleCheck")

        self.horizontalLayout_4.addWidget(self.upscaleDownscaleCheck)

        self.upscaleSpin = QSpinBox(self.upscaleTab)
        self.upscaleSpin.setObjectName(u"upscaleSpin")
        self.upscaleSpin.setMinimum(1)
        self.upscaleSpin.setValue(50)

        self.horizontalLayout_4.addWidget(self.upscaleSpin)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.tabWidget.addTab(self.upscaleTab, "")

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
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.imgDisplayIndex.setToolTip(QCoreApplication.translate("MainWindow", u"Image index", None))
#endif // QT_CONFIG(tooltip)
        self.imgDisplayIndex.setText(QCoreApplication.translate("MainWindow", u"----", None))
#if QT_CONFIG(tooltip)
        self.negPromptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter negative prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.negPromptLine.setPlainText(QCoreApplication.translate("MainWindow", u"ugly, bad quality, worst quality, frame, text, watermark", None))
        self.negPromptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Negative prompt", None))
#if QT_CONFIG(tooltip)
        self.promptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.negPromptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Negative prompt history", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.nextImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImgButton.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.nextImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.previousImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous image", None))
#endif // QT_CONFIG(tooltip)
        self.previousImgButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.promptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.promptLine.setPlainText(QCoreApplication.translate("MainWindow", u"cute rabbit in the snow, photograph", None))
        self.promptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.txt2imgTab), QCoreApplication.translate("MainWindow", u"Text to image", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.img2imgLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.img2imgDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.img2imgTab), QCoreApplication.translate("MainWindow", u"Image to image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.inpaintLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.inpaintDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open editor to create a masked image for inpainting", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setText(QCoreApplication.translate("MainWindow", u"Inpaint mask editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inpaintTab), QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.upscaleLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.upscaleDownscaleCheck.setText(QCoreApplication.translate("MainWindow", u"Downscale to:", None))
        self.upscaleSpin.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.upscaleTab), QCoreApplication.translate("MainWindow", u"Upscale", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

