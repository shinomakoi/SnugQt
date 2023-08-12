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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
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
        self.imgDisplayIndex = QLabel(self.centralwidget)
        self.imgDisplayIndex.setObjectName(u"imgDisplayIndex")

        self.gridLayout.addWidget(self.imgDisplayIndex, 1, 2, 1, 2, Qt.AlignHCenter)

        self.promptLine = QPlainTextEdit(self.centralwidget)
        self.promptLine.setObjectName(u"promptLine")

        self.gridLayout.addWidget(self.promptLine, 2, 0, 2, 1)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setMinimumSize(QSize(0, 64))
        font = QFont()
        font.setBold(True)
        self.generateButton.setFont(font)

        self.gridLayout.addWidget(self.generateButton, 3, 2, 1, 2)

        self.previousImgButton = QPushButton(self.centralwidget)
        self.previousImgButton.setObjectName(u"previousImgButton")

        self.gridLayout.addWidget(self.previousImgButton, 2, 2, 1, 1)

        self.negPromptHistoryCombo = QComboBox(self.centralwidget)
        self.negPromptHistoryCombo.setObjectName(u"negPromptHistoryCombo")

        self.gridLayout.addWidget(self.negPromptHistoryCombo, 1, 1, 1, 1)

        self.negPromptLine = QPlainTextEdit(self.centralwidget)
        self.negPromptLine.setObjectName(u"negPromptLine")

        self.gridLayout.addWidget(self.negPromptLine, 2, 1, 2, 1)

        self.promptHistoryCombo = QComboBox(self.centralwidget)
        self.promptHistoryCombo.setObjectName(u"promptHistoryCombo")

        self.gridLayout.addWidget(self.promptHistoryCombo, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1154, 957))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.imgLabel = QLabel(self.scrollAreaWidgetContents)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setAlignment(Qt.AlignCenter)
        self.imgLabel.setWordWrap(False)

        self.gridLayout_3.addWidget(self.imgLabel, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 4)

        self.nextImgButton = QPushButton(self.centralwidget)
        self.nextImgButton.setObjectName(u"nextImgButton")

        self.gridLayout.addWidget(self.nextImgButton, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 23))
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
        QWidget.setTabOrder(self.generateButton, self.scrollArea)

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
        self.imgDisplayIndex.setToolTip(QCoreApplication.translate("MainWindow", u"Image index", None))
#endif // QT_CONFIG(tooltip)
        self.imgDisplayIndex.setText(QCoreApplication.translate("MainWindow", u"----", None))
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
        self.previousImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Previous image", None))
#endif // QT_CONFIG(tooltip)
        self.previousImgButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(shortcut)
        self.previousImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
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
        self.promptHistoryCombo.setToolTip(QCoreApplication.translate("MainWindow", u"Prompt history", None))
#endif // QT_CONFIG(tooltip)
        self.imgLabel.setText(QCoreApplication.translate("MainWindow", u"Image display", None))
#if QT_CONFIG(tooltip)
        self.nextImgButton.setToolTip(QCoreApplication.translate("MainWindow", u"Next image", None))
#endif // QT_CONFIG(tooltip)
        self.nextImgButton.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(shortcut)
        self.nextImgButton.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

