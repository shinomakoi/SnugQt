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
    QGraphicsView, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStatusBar, QToolBox, QToolButton,
    QWidget)

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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.promptHistoryCombo = QComboBox(self.centralwidget)
        self.promptHistoryCombo.setObjectName(u"promptHistoryCombo")

        self.gridLayout.addWidget(self.promptHistoryCombo, 1, 0, 1, 1)

        self.nextImgButton = QPushButton(self.centralwidget)
        self.nextImgButton.setObjectName(u"nextImgButton")

        self.gridLayout.addWidget(self.nextImgButton, 2, 3, 1, 1)

        self.promptLine = QPlainTextEdit(self.centralwidget)
        self.promptLine.setObjectName(u"promptLine")

        self.gridLayout.addWidget(self.promptLine, 2, 0, 2, 1, Qt.AlignBottom)

        self.imgDisplayIndex = QLabel(self.centralwidget)
        self.imgDisplayIndex.setObjectName(u"imgDisplayIndex")

        self.gridLayout.addWidget(self.imgDisplayIndex, 1, 2, 1, 2, Qt.AlignHCenter)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setBold(True)
        self.generateButton.setFont(font)

        self.gridLayout.addWidget(self.generateButton, 3, 2, 1, 2)

        self.negPromptHistoryCombo = QComboBox(self.centralwidget)
        self.negPromptHistoryCombo.setObjectName(u"negPromptHistoryCombo")

        self.gridLayout.addWidget(self.negPromptHistoryCombo, 1, 1, 1, 1)

        self.negPromptLine = QPlainTextEdit(self.centralwidget)
        self.negPromptLine.setObjectName(u"negPromptLine")

        self.gridLayout.addWidget(self.negPromptLine, 2, 1, 2, 1, Qt.AlignBottom)

        self.previousImgButton = QPushButton(self.centralwidget)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 2, 2, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabWidget = QToolBox(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.toolBoxPage3 = QWidget()
        self.toolBoxPage3.setObjectName(u"toolBoxPage3")
        self.gridLayout_2 = QGridLayout(self.toolBoxPage3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.toolBoxPage3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 2, 1, 1)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.toolBoxPage3)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(4.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.050000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.gridLayout_2.addWidget(self.hiresfixScaleByValue, 2, 2, 1, 1)

        self.hiresfixStepsValue = QSpinBox(self.toolBoxPage3)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(256)
        self.hiresfixStepsValue.setValue(12)

        self.gridLayout_2.addWidget(self.hiresfixStepsValue, 4, 2, 1, 1)

        self.label = QLabel(self.toolBoxPage3)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 5, 2, 1, 1)

        self.label_2 = QLabel(self.toolBoxPage3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)

        self.hiresFixCheck = QCheckBox(self.toolBoxPage3)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.gridLayout_2.addWidget(self.hiresFixCheck, 0, 2, 1, 1)

        self.hiresfixDenoiseSpin = QDoubleSpinBox(self.toolBoxPage3)
        self.hiresfixDenoiseSpin.setObjectName(u"hiresfixDenoiseSpin")
        self.hiresfixDenoiseSpin.setMaximum(1.000000000000000)
        self.hiresfixDenoiseSpin.setSingleStep(0.050000000000000)
        self.hiresfixDenoiseSpin.setValue(0.600000000000000)

        self.gridLayout_2.addWidget(self.hiresfixDenoiseSpin, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 2, 1, 1)

        self.promptStyleCombo = QComboBox(self.toolBoxPage3)
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

        self.gridLayout_2.addWidget(self.promptStyleCombo, 8, 2, 1, 1)

        self.label_6 = QLabel(self.toolBoxPage3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 2, 1, 1)

        self.tabWidget.addItem(self.toolBoxPage3, u"Text to image")
        self.toolBoxPage2 = QWidget()
        self.toolBoxPage2.setObjectName(u"toolBoxPage2")
        self.gridLayout_3 = QGridLayout(self.toolBoxPage2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.img2imgLoadButton = QToolButton(self.toolBoxPage2)
        self.img2imgLoadButton.setObjectName(u"img2imgLoadButton")

        self.gridLayout_3.addWidget(self.img2imgLoadButton, 1, 1, 1, 1)

        self.label_3 = QLabel(self.toolBoxPage2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_29 = QLabel(self.toolBoxPage2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 3, 0, 1, 1)

        self.img2imgLoadLine = QLineEdit(self.toolBoxPage2)
        self.img2imgLoadLine.setObjectName(u"img2imgLoadLine")

        self.gridLayout_3.addWidget(self.img2imgLoadLine, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.img2imgDenoiseSpin = QDoubleSpinBox(self.toolBoxPage2)
        self.img2imgDenoiseSpin.setObjectName(u"img2imgDenoiseSpin")
        self.img2imgDenoiseSpin.setMaximum(1.000000000000000)
        self.img2imgDenoiseSpin.setSingleStep(0.050000000000000)
        self.img2imgDenoiseSpin.setValue(0.700000000000000)

        self.gridLayout_3.addWidget(self.img2imgDenoiseSpin, 4, 0, 1, 2)

        self.tabWidget.addItem(self.toolBoxPage2, u"Image to image")
        self.inpaint = QWidget()
        self.inpaint.setObjectName(u"inpaint")
        self.gridLayout_4 = QGridLayout(self.inpaint)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inpaintLoadButton = QToolButton(self.inpaint)
        self.inpaintLoadButton.setObjectName(u"inpaintLoadButton")

        self.gridLayout_4.addWidget(self.inpaintLoadButton, 4, 2, 1, 1)

        self.label_26 = QLabel(self.inpaint)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_4 = QLabel(self.inpaint)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 4, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.inpaintMaskEditorButton = QPushButton(self.inpaint)
        self.inpaintMaskEditorButton.setObjectName(u"inpaintMaskEditorButton")

        self.gridLayout_4.addWidget(self.inpaintMaskEditorButton, 7, 0, 1, 3)

        self.inpaintDenoiseSpin = QDoubleSpinBox(self.inpaint)
        self.inpaintDenoiseSpin.setObjectName(u"inpaintDenoiseSpin")
        self.inpaintDenoiseSpin.setMaximum(1.000000000000000)
        self.inpaintDenoiseSpin.setSingleStep(0.050000000000000)
        self.inpaintDenoiseSpin.setValue(0.900000000000000)

        self.gridLayout_4.addWidget(self.inpaintDenoiseSpin, 6, 0, 1, 3)

        self.inpaintLoadLine = QLineEdit(self.inpaint)
        self.inpaintLoadLine.setObjectName(u"inpaintLoadLine")

        self.gridLayout_4.addWidget(self.inpaintLoadLine, 4, 0, 1, 2)

        self.tabWidget.addItem(self.inpaint, u"Inpainting")
        self.upscale = QWidget()
        self.upscale.setObjectName(u"upscale")
        self.gridLayout_5 = QGridLayout(self.upscale)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.upscaleLoadLine = QLineEdit(self.upscale)
        self.upscaleLoadLine.setObjectName(u"upscaleLoadLine")

        self.gridLayout_5.addWidget(self.upscaleLoadLine, 1, 0, 1, 1)

        self.upscaleDownscaleCheck = QCheckBox(self.upscale)
        self.upscaleDownscaleCheck.setObjectName(u"upscaleDownscaleCheck")

        self.gridLayout_5.addWidget(self.upscaleDownscaleCheck, 2, 0, 1, 1)

        self.label_5 = QLabel(self.upscale)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.upscaleLoadButton = QToolButton(self.upscale)
        self.upscaleLoadButton.setObjectName(u"upscaleLoadButton")

        self.gridLayout_5.addWidget(self.upscaleLoadButton, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.upscaleSpin = QSpinBox(self.upscale)
        self.upscaleSpin.setObjectName(u"upscaleSpin")
        self.upscaleSpin.setMinimum(1)
        self.upscaleSpin.setValue(50)

        self.gridLayout_5.addWidget(self.upscaleSpin, 3, 0, 1, 2)

        self.tabWidget.addItem(self.upscale, u"Upscale")
        self.splitter.addWidget(self.tabWidget)
        self.imageView = QGraphicsView(self.splitter)
        self.imageView.setObjectName(u"imageView")
        self.imageView.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.splitter.addWidget(self.imageView)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1445, 27))
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
        self.nextImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImgButton.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.nextImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.promptLine.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the prompt here", None))
#endif // QT_CONFIG(tooltip)
        self.promptLine.setPlainText(QCoreApplication.translate("MainWindow", u"cute rabbit in the snow, photograph", None))
        self.promptLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt", None))
#if QT_CONFIG(tooltip)
        self.imgDisplayIndex.setToolTip(QCoreApplication.translate("MainWindow", u"Image index", None))
#endif // QT_CONFIG(tooltip)
        self.imgDisplayIndex.setText(QCoreApplication.translate("MainWindow", u"----", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Generate images", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.negPromptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Negative prompt history", None))
#endif // QT_CONFIG(tooltip)
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
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix steps:", None))
#if QT_CONFIG(tooltip)
        self.hiresfixScaleByValue.setToolTip(QCoreApplication.translate("MainWindow", u"Factor to scale hires-fix image by", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Denoise:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Upscale by:", None))
#if QT_CONFIG(tooltip)
        self.hiresFixCheck.setToolTip(QCoreApplication.translate("MainWindow", u"Enable hi-res fix", None))
#endif // QT_CONFIG(tooltip)
        self.hiresFixCheck.setText(QCoreApplication.translate("MainWindow", u"Hi-res fix", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Style:", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.toolBoxPage3), QCoreApplication.translate("MainWindow", u"Text to image", None))
        self.img2imgLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.img2imgDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.toolBoxPage2), QCoreApplication.translate("MainWindow", u"Image to image", None))
        self.inpaintLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Denoise strength:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
#if QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setToolTip(QCoreApplication.translate("MainWindow", u"Open editor to create a masked image for inpainting", None))
#endif // QT_CONFIG(tooltip)
        self.inpaintMaskEditorButton.setText(QCoreApplication.translate("MainWindow", u"Inpaint mask editor", None))
#if QT_CONFIG(tooltip)
        self.inpaintDenoiseSpin.setToolTip(QCoreApplication.translate("MainWindow", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.inpaint), QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.upscaleDownscaleCheck.setText(QCoreApplication.translate("MainWindow", u"Downscale to:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Image:", None))
        self.upscaleLoadButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.upscaleSpin.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.tabWidget.setItemText(self.tabWidget.indexOf(self.upscale), QCoreApplication.translate("MainWindow", u"Upscale", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

