# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QToolButton, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(664, 819)
        self.gridLayout = QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveSettingsButton = QPushButton(SettingsDialog)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")

        self.gridLayout.addWidget(self.saveSettingsButton, 2, 0, 1, 1)

        self.settingsTab = QTabWidget(SettingsDialog)
        self.settingsTab.setObjectName(u"settingsTab")
        self.parametersTab = QWidget()
        self.parametersTab.setObjectName(u"parametersTab")
        self.parametersTab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.parametersTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_20 = QLabel(self.parametersTab)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 17, 0, 1, 1)

        self.label_16 = QLabel(self.parametersTab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 31, 0, 1, 1)

        self.label_5 = QLabel(self.parametersTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 23, 0, 1, 1)

        self.label_14 = QLabel(self.parametersTab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.sdxlRefinerCheck = QCheckBox(self.parametersTab)
        self.sdxlRefinerCheck.setObjectName(u"sdxlRefinerCheck")

        self.gridLayout_4.addWidget(self.sdxlRefinerCheck, 30, 0, 1, 1)

        self.modelUpscaleCheck = QCheckBox(self.parametersTab)
        self.modelUpscaleCheck.setObjectName(u"modelUpscaleCheck")

        self.gridLayout_4.addWidget(self.modelUpscaleCheck, 40, 0, 1, 1)

        self.iterationsValue = QSpinBox(self.parametersTab)
        self.iterationsValue.setObjectName(u"iterationsValue")
        self.iterationsValue.setMinimum(1)
        self.iterationsValue.setMaximum(128)

        self.gridLayout_4.addWidget(self.iterationsValue, 17, 1, 1, 1)

        self.imgWidthValue = QSpinBox(self.parametersTab)
        self.imgWidthValue.setObjectName(u"imgWidthValue")
        self.imgWidthValue.setMinimum(256)
        self.imgWidthValue.setMaximum(4096)
        self.imgWidthValue.setSingleStep(64)
        self.imgWidthValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgWidthValue, 5, 1, 1, 1)

        self.cfgValue = QSpinBox(self.parametersTab)
        self.cfgValue.setObjectName(u"cfgValue")
        self.cfgValue.setMinimum(1)
        self.cfgValue.setMaximum(40)
        self.cfgValue.setValue(8)

        self.gridLayout_4.addWidget(self.cfgValue, 19, 1, 1, 1)

        self.label = QLabel(self.parametersTab)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 16, 0, 1, 1)

        self.seedValue = QSpinBox(self.parametersTab)
        self.seedValue.setObjectName(u"seedValue")
        self.seedValue.setMinimum(-1)
        self.seedValue.setMaximum(999999999)
        self.seedValue.setValue(-1)

        self.gridLayout_4.addWidget(self.seedValue, 16, 1, 1, 1)

        self.schedulerValue = QComboBox(self.parametersTab)
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.setObjectName(u"schedulerValue")

        self.gridLayout_4.addWidget(self.schedulerValue, 24, 1, 1, 2)

        self.batchValue = QSpinBox(self.parametersTab)
        self.batchValue.setObjectName(u"batchValue")
        self.batchValue.setMinimum(1)
        self.batchValue.setMaximum(64)
        self.batchValue.setValue(2)

        self.gridLayout_4.addWidget(self.batchValue, 18, 1, 1, 1)

        self.label_3 = QLabel(self.parametersTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 18, 0, 1, 1)

        self.samplerValue = QComboBox(self.parametersTab)
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.setObjectName(u"samplerValue")

        self.gridLayout_4.addWidget(self.samplerValue, 23, 1, 1, 2)

        self.hiresfixScaleByValue = QDoubleSpinBox(self.parametersTab)
        self.hiresfixScaleByValue.setObjectName(u"hiresfixScaleByValue")
        self.hiresfixScaleByValue.setDecimals(2)
        self.hiresfixScaleByValue.setMinimum(1.000000000000000)
        self.hiresfixScaleByValue.setMaximum(4.000000000000000)
        self.hiresfixScaleByValue.setSingleStep(0.050000000000000)
        self.hiresfixScaleByValue.setValue(1.400000000000000)

        self.gridLayout_4.addWidget(self.hiresfixScaleByValue, 42, 1, 1, 1)

        self.label_10 = QLabel(self.parametersTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)

        self.hiresFixCheck = QCheckBox(self.parametersTab)
        self.hiresFixCheck.setObjectName(u"hiresFixCheck")

        self.gridLayout_4.addWidget(self.hiresFixCheck, 41, 0, 1, 1)

        self.hiresfixStepsValue = QSpinBox(self.parametersTab)
        self.hiresfixStepsValue.setObjectName(u"hiresfixStepsValue")
        self.hiresfixStepsValue.setMinimum(1)
        self.hiresfixStepsValue.setMaximum(256)
        self.hiresfixStepsValue.setValue(12)

        self.gridLayout_4.addWidget(self.hiresfixStepsValue, 43, 1, 1, 1)

        self.label_9 = QLabel(self.parametersTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 1)

        self.modelUpscaleCombo = QComboBox(self.parametersTab)
        self.modelUpscaleCombo.setObjectName(u"modelUpscaleCombo")

        self.gridLayout_4.addWidget(self.modelUpscaleCombo, 40, 1, 1, 2)

        self.label_2 = QLabel(self.parametersTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 42, 0, 1, 1)

        self.label_6 = QLabel(self.parametersTab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 24, 0, 1, 1)

        self.line_2 = QFrame(self.parametersTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 39, 0, 1, 3)

        self.useExternalVaeCheck = QCheckBox(self.parametersTab)
        self.useExternalVaeCheck.setObjectName(u"useExternalVaeCheck")

        self.gridLayout_4.addWidget(self.useExternalVaeCheck, 3, 0, 1, 1)

        self.line_4 = QFrame(self.parametersTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 4, 0, 1, 3)

        self.imgHeightValue = QSpinBox(self.parametersTab)
        self.imgHeightValue.setObjectName(u"imgHeightValue")
        self.imgHeightValue.setMinimum(256)
        self.imgHeightValue.setMaximum(4096)
        self.imgHeightValue.setSingleStep(64)
        self.imgHeightValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgHeightValue, 6, 1, 1, 1)

        self.label_13 = QLabel(self.parametersTab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 43, 0, 1, 1)

        self.label_7 = QLabel(self.parametersTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 20, 0, 1, 1)

        self.label_4 = QLabel(self.parametersTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 19, 0, 1, 1)

        self.line_3 = QFrame(self.parametersTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 29, 0, 1, 3)

        self.stepsValue = QSpinBox(self.parametersTab)
        self.stepsValue.setObjectName(u"stepsValue")
        self.stepsValue.setMinimum(1)
        self.stepsValue.setMaximum(400)
        self.stepsValue.setValue(20)

        self.gridLayout_4.addWidget(self.stepsValue, 20, 1, 1, 1)

        self.sdxlRefinerStepsValue = QSpinBox(self.parametersTab)
        self.sdxlRefinerStepsValue.setObjectName(u"sdxlRefinerStepsValue")
        self.sdxlRefinerStepsValue.setMinimum(1)
        self.sdxlRefinerStepsValue.setMaximum(200)
        self.sdxlRefinerStepsValue.setValue(5)

        self.gridLayout_4.addWidget(self.sdxlRefinerStepsValue, 31, 1, 1, 1)

        self.modeSelectCombo = QComboBox(self.parametersTab)
        self.modeSelectCombo.addItem("")
        self.modeSelectCombo.addItem("")
        self.modeSelectCombo.setObjectName(u"modeSelectCombo")

        self.gridLayout_4.addWidget(self.modeSelectCombo, 1, 1, 1, 2)

        self.label_25 = QLabel(self.parametersTab)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 25, 0, 1, 1)

        self.clipSkipValue = QSpinBox(self.parametersTab)
        self.clipSkipValue.setObjectName(u"clipSkipValue")
        self.clipSkipValue.setMinimum(-8)
        self.clipSkipValue.setMaximum(-1)

        self.gridLayout_4.addWidget(self.clipSkipValue, 25, 1, 1, 1)

        self.settingsTab.addTab(self.parametersTab, "")
        self.img2imgTab = QWidget()
        self.img2imgTab.setObjectName(u"img2imgTab")
        self.img2imgTab.setAutoFillBackground(True)
        self.gridLayout_5 = QGridLayout(self.img2imgTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_26 = QLabel(self.img2imgTab)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 2, 1, 1, 1)

        self.img2imgCheck = QCheckBox(self.img2imgTab)
        self.img2imgCheck.setObjectName(u"img2imgCheck")

        self.gridLayout_5.addWidget(self.img2imgCheck, 0, 1, 1, 1)

        self.img2imgLoadButton = QToolButton(self.img2imgTab)
        self.img2imgLoadButton.setObjectName(u"img2imgLoadButton")
        self.img2imgLoadButton.setArrowType(Qt.RightArrow)

        self.gridLayout_5.addWidget(self.img2imgLoadButton, 1, 4, 1, 1)

        self.img2imgLoadCombo = QComboBox(self.img2imgTab)
        self.img2imgLoadCombo.setObjectName(u"img2imgLoadCombo")

        self.gridLayout_5.addWidget(self.img2imgLoadCombo, 1, 2, 1, 1)

        self.img2imgDenoiseSpin = QDoubleSpinBox(self.img2imgTab)
        self.img2imgDenoiseSpin.setObjectName(u"img2imgDenoiseSpin")
        self.img2imgDenoiseSpin.setMaximum(1.000000000000000)
        self.img2imgDenoiseSpin.setSingleStep(0.050000000000000)
        self.img2imgDenoiseSpin.setValue(0.700000000000000)

        self.gridLayout_5.addWidget(self.img2imgDenoiseSpin, 2, 2, 1, 1)

        self.label_27 = QLabel(self.img2imgTab)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 1, 1, 1, 1)

        self.settingsTab.addTab(self.img2imgTab, "")
        self.loraTab = QWidget()
        self.loraTab.setObjectName(u"loraTab")
        self.loraTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.loraTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sdxlLoraCombo = QComboBox(self.loraTab)
        self.sdxlLoraCombo.setObjectName(u"sdxlLoraCombo")

        self.gridLayout_3.addWidget(self.sdxlLoraCombo, 2, 3, 1, 1)

        self.label_21 = QLabel(self.loraTab)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 6, 0, 1, 1)

        self.label_24 = QLabel(self.loraTab)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)

        self.sd12LoraCombo = QComboBox(self.loraTab)
        self.sd12LoraCombo.setObjectName(u"sd12LoraCombo")

        self.gridLayout_3.addWidget(self.sd12LoraCombo, 1, 3, 1, 1)

        self.loraCheck = QCheckBox(self.loraTab)
        self.loraCheck.setObjectName(u"loraCheck")

        self.gridLayout_3.addWidget(self.loraCheck, 0, 0, 1, 1)

        self.label_23 = QLabel(self.loraTab)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 5, 0, 1, 1)

        self.loraClipStrengthSpin = QDoubleSpinBox(self.loraTab)
        self.loraClipStrengthSpin.setObjectName(u"loraClipStrengthSpin")
        self.loraClipStrengthSpin.setMaximum(2.000000000000000)
        self.loraClipStrengthSpin.setSingleStep(0.050000000000000)
        self.loraClipStrengthSpin.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.loraClipStrengthSpin, 6, 3, 1, 1)

        self.loraStrengthSpin = QDoubleSpinBox(self.loraTab)
        self.loraStrengthSpin.setObjectName(u"loraStrengthSpin")
        self.loraStrengthSpin.setMaximum(2.000000000000000)
        self.loraStrengthSpin.setSingleStep(0.050000000000000)
        self.loraStrengthSpin.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.loraStrengthSpin, 5, 3, 1, 1)

        self.label_22 = QLabel(self.loraTab)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)

        self.line_7 = QFrame(self.loraTab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 3, 3, 1, 1)

        self.settingsTab.addTab(self.loraTab, "")
        self.modelsTab = QWidget()
        self.modelsTab.setObjectName(u"modelsTab")
        self.modelsTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.modelsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comfyuiModelFolderValue = QLineEdit(self.modelsTab)
        self.comfyuiModelFolderValue.setObjectName(u"comfyuiModelFolderValue")
        self.comfyuiModelFolderValue.setReadOnly(True)

        self.gridLayout_2.addWidget(self.comfyuiModelFolderValue, 0, 1, 1, 1)

        self.comfyuiModelFolderSelect = QToolButton(self.modelsTab)
        self.comfyuiModelFolderSelect.setObjectName(u"comfyuiModelFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiModelFolderSelect, 0, 3, 1, 1)

        self.line_5 = QFrame(self.modelsTab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 13, 1, 1, 1)

        self.comfyuiExtraFolderSelect = QToolButton(self.modelsTab)
        self.comfyuiExtraFolderSelect.setObjectName(u"comfyuiExtraFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiExtraFolderSelect, 1, 3, 1, 1)

        self.sdxlBaseCheckpointCombo = QComboBox(self.modelsTab)
        self.sdxlBaseCheckpointCombo.setObjectName(u"sdxlBaseCheckpointCombo")

        self.gridLayout_2.addWidget(self.sdxlBaseCheckpointCombo, 11, 1, 1, 3)

        self.sd12CheckpointCombo = QComboBox(self.modelsTab)
        self.sd12CheckpointCombo.setObjectName(u"sd12CheckpointCombo")

        self.gridLayout_2.addWidget(self.sd12CheckpointCombo, 9, 1, 1, 3)

        self.line_6 = QFrame(self.modelsTab)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 8, 1, 1, 1)

        self.label_19 = QLabel(self.modelsTab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)

        self.comfyuiExtraFolderValue = QLineEdit(self.modelsTab)
        self.comfyuiExtraFolderValue.setObjectName(u"comfyuiExtraFolderValue")
        self.comfyuiExtraFolderValue.setReadOnly(True)

        self.gridLayout_2.addWidget(self.comfyuiExtraFolderValue, 1, 1, 1, 1)

        self.label_15 = QLabel(self.modelsTab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_12 = QLabel(self.modelsTab)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 12, 0, 1, 1)

        self.sdxlRefinerCheckpointCombo = QComboBox(self.modelsTab)
        self.sdxlRefinerCheckpointCombo.setObjectName(u"sdxlRefinerCheckpointCombo")

        self.gridLayout_2.addWidget(self.sdxlRefinerCheckpointCombo, 12, 1, 1, 3)

        self.label_17 = QLabel(self.modelsTab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 14, 0, 1, 1)

        self.label_8 = QLabel(self.modelsTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 9, 0, 1, 1)

        self.sd12VaeCombo = QComboBox(self.modelsTab)
        self.sd12VaeCombo.setObjectName(u"sd12VaeCombo")

        self.gridLayout_2.addWidget(self.sd12VaeCombo, 14, 1, 1, 3)

        self.sdxlVaeCombo = QComboBox(self.modelsTab)
        self.sdxlVaeCombo.setObjectName(u"sdxlVaeCombo")

        self.gridLayout_2.addWidget(self.sdxlVaeCombo, 15, 1, 1, 3)

        self.label_18 = QLabel(self.modelsTab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 15, 0, 1, 1)

        self.label_11 = QLabel(self.modelsTab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 11, 0, 1, 1)

        self.reloadModelsButton = QPushButton(self.modelsTab)
        self.reloadModelsButton.setObjectName(u"reloadModelsButton")

        self.gridLayout_2.addWidget(self.reloadModelsButton, 2, 0, 1, 1)

        self.settingsTab.addTab(self.modelsTab, "")

        self.gridLayout.addWidget(self.settingsTab, 1, 0, 1, 1)

        QWidget.setTabOrder(self.useExternalVaeCheck, self.imgWidthValue)
        QWidget.setTabOrder(self.imgWidthValue, self.imgHeightValue)
        QWidget.setTabOrder(self.imgHeightValue, self.seedValue)
        QWidget.setTabOrder(self.seedValue, self.iterationsValue)
        QWidget.setTabOrder(self.iterationsValue, self.batchValue)
        QWidget.setTabOrder(self.batchValue, self.cfgValue)
        QWidget.setTabOrder(self.cfgValue, self.stepsValue)
        QWidget.setTabOrder(self.stepsValue, self.loraCheck)
        QWidget.setTabOrder(self.loraCheck, self.sd12LoraCombo)
        QWidget.setTabOrder(self.sd12LoraCombo, self.sdxlLoraCombo)
        QWidget.setTabOrder(self.sdxlLoraCombo, self.loraStrengthSpin)
        QWidget.setTabOrder(self.loraStrengthSpin, self.loraClipStrengthSpin)
        QWidget.setTabOrder(self.loraClipStrengthSpin, self.modeSelectCombo)
        QWidget.setTabOrder(self.modeSelectCombo, self.comfyuiModelFolderValue)
        QWidget.setTabOrder(self.comfyuiModelFolderValue, self.comfyuiModelFolderSelect)
        QWidget.setTabOrder(self.comfyuiModelFolderSelect, self.comfyuiExtraFolderValue)
        QWidget.setTabOrder(self.comfyuiExtraFolderValue, self.comfyuiExtraFolderSelect)
        QWidget.setTabOrder(self.comfyuiExtraFolderSelect, self.sd12CheckpointCombo)
        QWidget.setTabOrder(self.sd12CheckpointCombo, self.sdxlBaseCheckpointCombo)
        QWidget.setTabOrder(self.sdxlBaseCheckpointCombo, self.sdxlRefinerCheckpointCombo)
        QWidget.setTabOrder(self.sdxlRefinerCheckpointCombo, self.sd12VaeCombo)
        QWidget.setTabOrder(self.sd12VaeCombo, self.sdxlVaeCombo)
        QWidget.setTabOrder(self.sdxlVaeCombo, self.saveSettingsButton)

        self.retranslateUi(SettingsDialog)

        self.settingsTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"SnugQt - Settings", None))
#if QT_CONFIG(tooltip)
        self.saveSettingsButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Save the current settings", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingsButton.setText(QCoreApplication.translate("SettingsDialog", u"Save settings", None))
        self.label_20.setText(QCoreApplication.translate("SettingsDialog", u"Iterations:", None))
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"SDXL refiner steps:", None))
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Sampler:", None))
        self.label_14.setText(QCoreApplication.translate("SettingsDialog", u"Mode:", None))
#if QT_CONFIG(tooltip)
        self.sdxlRefinerCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable refiner when using SDXL", None))
#endif // QT_CONFIG(tooltip)
        self.sdxlRefinerCheck.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Refiner", None))
#if QT_CONFIG(tooltip)
        self.modelUpscaleCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Upscale final image with upscale model", None))
#endif // QT_CONFIG(tooltip)
        self.modelUpscaleCheck.setText(QCoreApplication.translate("SettingsDialog", u"Upscale with model:", None))
#if QT_CONFIG(tooltip)
        self.iterationsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of iterations to perform", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.imgWidthValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Width of the generated image", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cfgValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"CFG scale value", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Seed:", None))
#if QT_CONFIG(tooltip)
        self.seedValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Seed to use. -1 for random", None))
#endif // QT_CONFIG(tooltip)
        self.schedulerValue.setItemText(0, QCoreApplication.translate("SettingsDialog", u"normal", None))
        self.schedulerValue.setItemText(1, QCoreApplication.translate("SettingsDialog", u"karras", None))
        self.schedulerValue.setItemText(2, QCoreApplication.translate("SettingsDialog", u"exponential", None))
        self.schedulerValue.setItemText(3, QCoreApplication.translate("SettingsDialog", u"simple", None))
        self.schedulerValue.setItemText(4, QCoreApplication.translate("SettingsDialog", u"ddim_uniform", None))

#if QT_CONFIG(tooltip)
        self.schedulerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise scheduler to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.batchValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"How many images to generate at once. More VRAM", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Batch size:", None))
        self.samplerValue.setItemText(0, QCoreApplication.translate("SettingsDialog", u"euler", None))
        self.samplerValue.setItemText(1, QCoreApplication.translate("SettingsDialog", u"euler_ancestral", None))
        self.samplerValue.setItemText(2, QCoreApplication.translate("SettingsDialog", u"heun", None))
        self.samplerValue.setItemText(3, QCoreApplication.translate("SettingsDialog", u"dpm_2", None))
        self.samplerValue.setItemText(4, QCoreApplication.translate("SettingsDialog", u"dpm_2_ancestral", None))
        self.samplerValue.setItemText(5, QCoreApplication.translate("SettingsDialog", u"lms", None))
        self.samplerValue.setItemText(6, QCoreApplication.translate("SettingsDialog", u"dpmpp_2s_ancestral", None))
        self.samplerValue.setItemText(7, QCoreApplication.translate("SettingsDialog", u"dpmpp_sde", None))
        self.samplerValue.setItemText(8, QCoreApplication.translate("SettingsDialog", u"dpmpp_sde_gpu", None))
        self.samplerValue.setItemText(9, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m", None))
        self.samplerValue.setItemText(10, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m_sde", None))
        self.samplerValue.setItemText(11, QCoreApplication.translate("SettingsDialog", u"dpmpp_2m_sde_gpu", None))
        self.samplerValue.setItemText(12, QCoreApplication.translate("SettingsDialog", u"ddim", None))
        self.samplerValue.setItemText(13, QCoreApplication.translate("SettingsDialog", u"uni_pc", None))
        self.samplerValue.setItemText(14, QCoreApplication.translate("SettingsDialog", u"uni_pc_bh2", None))

#if QT_CONFIG(tooltip)
        self.samplerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise sampler to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.hiresfixScaleByValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Factor to scale hires-fix image by", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Height:", None))
#if QT_CONFIG(tooltip)
        self.hiresFixCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable hi-res fix", None))
#endif // QT_CONFIG(tooltip)
        self.hiresFixCheck.setText(QCoreApplication.translate("SettingsDialog", u"Hi-res fix", None))
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Width:", None))
#if QT_CONFIG(tooltip)
        self.modelUpscaleCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Upscale model to use", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Upscale by:", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Scheduler:", None))
#if QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Use an external VAE instead of model's built-in VAE", None))
#endif // QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setText(QCoreApplication.translate("SettingsDialog", u"Use external VAE", None))
#if QT_CONFIG(tooltip)
        self.imgHeightValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Height of the generated image", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"Hi-res fix steps:", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Steps:", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"CFG scale:", None))
#if QT_CONFIG(tooltip)
        self.stepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform when generating iamge", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlRefinerStepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform with SDXL refiner", None))
#endif // QT_CONFIG(tooltip)
        self.modeSelectCombo.setItemText(0, QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2", None))
        self.modeSelectCombo.setItemText(1, QCoreApplication.translate("SettingsDialog", u"SDXL", None))

#if QT_CONFIG(tooltip)
        self.modeSelectCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the model type", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("SettingsDialog", u"Clip skip:", None))
#if QT_CONFIG(tooltip)
        self.clipSkipValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Set last layer of CLIP. -1 for normal", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.parametersTab), QCoreApplication.translate("SettingsDialog", u"Parameters", None))
        self.label_26.setText(QCoreApplication.translate("SettingsDialog", u"Denoise strength:", None))
#if QT_CONFIG(tooltip)
        self.img2imgCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Start with an image instead of empty latent noise", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgCheck.setText(QCoreApplication.translate("SettingsDialog", u"Enable Image to Image", None))
#if QT_CONFIG(tooltip)
        self.img2imgLoadButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Load images from ComfyUI/input folder", None))
#endif // QT_CONFIG(tooltip)
        self.img2imgLoadButton.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.img2imgDenoiseSpin.setToolTip(QCoreApplication.translate("SettingsDialog", u"Denoising strength. Higher value = less like starting image", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("SettingsDialog", u"Load image:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.img2imgTab), QCoreApplication.translate("SettingsDialog", u"Image to Image", None))
#if QT_CONFIG(tooltip)
        self.sdxlLoraCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SDXL LoRA", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("SettingsDialog", u"LoRA clip strength:", None))
        self.label_24.setText(QCoreApplication.translate("SettingsDialog", u"SD1/2 LoRA:", None))
#if QT_CONFIG(tooltip)
        self.sd12LoraCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 LoRA", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loraCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable a LoRA when generating images", None))
#endif // QT_CONFIG(tooltip)
        self.loraCheck.setText(QCoreApplication.translate("SettingsDialog", u"Enable LoRA", None))
        self.label_23.setText(QCoreApplication.translate("SettingsDialog", u"LoRA model strength:", None))
#if QT_CONFIG(tooltip)
        self.loraClipStrengthSpin.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the clip strength of the LoRA", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loraStrengthSpin.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the model strength of the LoRA", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("SettingsDialog", u"SDXL LoRA:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.loraTab), QCoreApplication.translate("SettingsDialog", u"LoRA", None))
#if QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to the 'ComfyUI/models' folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI/models", None))
#if QT_CONFIG(tooltip)
        self.comfyuiModelFolderSelect.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the 'ComfyUI/models' folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiModelFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.comfyuiExtraFolderSelect.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select a ComfyUI extra models folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiExtraFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.sdxlBaseCheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SDXL base model", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sd12CheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 checkpoint", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI extra checkpoints folder:", None))
#if QT_CONFIG(tooltip)
        self.comfyuiExtraFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to extra checkpoints folder, must be recognised by ComfyUI", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiExtraFolderValue.setText("")
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI models folder: ", None))
        self.label_12.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Refiner model:", None))
#if QT_CONFIG(tooltip)
        self.sdxlRefinerCheckpointCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the SDXL refiner model", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2 VAE:", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", u"Stable Diffusion 1/2 model:", None))
#if QT_CONFIG(tooltip)
        self.sd12VaeCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 external VAE", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlVaeCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the SDXL external VAE", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("SettingsDialog", u"SDXL VAE:", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Base model:", None))
#if QT_CONFIG(tooltip)
        self.reloadModelsButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Reload models", None))
#endif // QT_CONFIG(tooltip)
        self.reloadModelsButton.setText(QCoreApplication.translate("SettingsDialog", u"Reload", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.modelsTab), QCoreApplication.translate("SettingsDialog", u"Models", None))
    # retranslateUi

