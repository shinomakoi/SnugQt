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
        self.settingsTab.setDocumentMode(False)
        self.parametersTab = QWidget()
        self.parametersTab.setObjectName(u"parametersTab")
        self.parametersTab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.parametersTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.checkpointCombo = QComboBox(self.parametersTab)
        self.checkpointCombo.setObjectName(u"checkpointCombo")

        self.gridLayout_4.addWidget(self.checkpointCombo, 1, 1, 1, 2)

        self.line_2 = QFrame(self.parametersTab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 41, 0, 1, 3)

        self.label_9 = QLabel(self.parametersTab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)

        self.useExternalVaeCheck = QCheckBox(self.parametersTab)
        self.useExternalVaeCheck.setObjectName(u"useExternalVaeCheck")

        self.gridLayout_4.addWidget(self.useExternalVaeCheck, 2, 0, 1, 1)

        self.label_10 = QLabel(self.parametersTab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_6 = QLabel(self.parametersTab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 23, 0, 1, 1)

        self.sdxlRefinerStepsValue = QSpinBox(self.parametersTab)
        self.sdxlRefinerStepsValue.setObjectName(u"sdxlRefinerStepsValue")
        self.sdxlRefinerStepsValue.setMinimum(1)
        self.sdxlRefinerStepsValue.setMaximum(200)
        self.sdxlRefinerStepsValue.setValue(5)

        self.gridLayout_4.addWidget(self.sdxlRefinerStepsValue, 31, 1, 1, 1)

        self.sdxlRefinerCheck = QCheckBox(self.parametersTab)
        self.sdxlRefinerCheck.setObjectName(u"sdxlRefinerCheck")

        self.gridLayout_4.addWidget(self.sdxlRefinerCheck, 29, 0, 1, 1)

        self.line_4 = QFrame(self.parametersTab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 3, 0, 1, 3)

        self.modelUpscaleCheck = QCheckBox(self.parametersTab)
        self.modelUpscaleCheck.setObjectName(u"modelUpscaleCheck")

        self.gridLayout_4.addWidget(self.modelUpscaleCheck, 42, 0, 1, 1)

        self.stepsValue = QSpinBox(self.parametersTab)
        self.stepsValue.setObjectName(u"stepsValue")
        self.stepsValue.setMinimum(1)
        self.stepsValue.setMaximum(400)
        self.stepsValue.setValue(20)

        self.gridLayout_4.addWidget(self.stepsValue, 19, 1, 1, 1)

        self.modelUpscaleCombo = QComboBox(self.parametersTab)
        self.modelUpscaleCombo.setObjectName(u"modelUpscaleCombo")

        self.gridLayout_4.addWidget(self.modelUpscaleCombo, 42, 1, 1, 2)

        self.clipSkipValue = QSpinBox(self.parametersTab)
        self.clipSkipValue.setObjectName(u"clipSkipValue")
        self.clipSkipValue.setMinimum(-8)
        self.clipSkipValue.setMaximum(-1)

        self.gridLayout_4.addWidget(self.clipSkipValue, 24, 1, 1, 1)

        self.label_16 = QLabel(self.parametersTab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 31, 0, 1, 1)

        self.label_13 = QLabel(self.parametersTab)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 30, 0, 1, 1)

        self.label_20 = QLabel(self.parametersTab)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 16, 0, 1, 1)

        self.label_25 = QLabel(self.parametersTab)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 24, 0, 1, 1)

        self.externalVaeCombo = QComboBox(self.parametersTab)
        self.externalVaeCombo.setObjectName(u"externalVaeCombo")

        self.gridLayout_4.addWidget(self.externalVaeCombo, 2, 1, 1, 2)

        self.line_3 = QFrame(self.parametersTab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 28, 0, 1, 3)

        self.schedulerValue = QComboBox(self.parametersTab)
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.addItem("")
        self.schedulerValue.setObjectName(u"schedulerValue")

        self.gridLayout_4.addWidget(self.schedulerValue, 23, 1, 1, 2)

        self.imgWidthValue = QSpinBox(self.parametersTab)
        self.imgWidthValue.setObjectName(u"imgWidthValue")
        self.imgWidthValue.setMinimum(256)
        self.imgWidthValue.setMaximum(4096)
        self.imgWidthValue.setSingleStep(64)
        self.imgWidthValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgWidthValue, 4, 1, 1, 1)

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
        self.samplerValue.addItem("")
        self.samplerValue.addItem("")
        self.samplerValue.setObjectName(u"samplerValue")

        self.gridLayout_4.addWidget(self.samplerValue, 22, 1, 1, 2)

        self.iterationsValue = QSpinBox(self.parametersTab)
        self.iterationsValue.setObjectName(u"iterationsValue")
        self.iterationsValue.setMinimum(1)
        self.iterationsValue.setMaximum(128)

        self.gridLayout_4.addWidget(self.iterationsValue, 16, 1, 1, 1)

        self.label_5 = QLabel(self.parametersTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 22, 0, 1, 1)

        self.seedValue = QSpinBox(self.parametersTab)
        self.seedValue.setObjectName(u"seedValue")
        self.seedValue.setMinimum(-1)
        self.seedValue.setMaximum(999999999)
        self.seedValue.setValue(-1)

        self.gridLayout_4.addWidget(self.seedValue, 15, 1, 1, 1)

        self.imgHeightValue = QSpinBox(self.parametersTab)
        self.imgHeightValue.setObjectName(u"imgHeightValue")
        self.imgHeightValue.setMinimum(256)
        self.imgHeightValue.setMaximum(4096)
        self.imgHeightValue.setSingleStep(64)
        self.imgHeightValue.setValue(512)

        self.gridLayout_4.addWidget(self.imgHeightValue, 5, 1, 1, 1)

        self.sdxlRefinerCheckpointCombo = QComboBox(self.parametersTab)
        self.sdxlRefinerCheckpointCombo.setObjectName(u"sdxlRefinerCheckpointCombo")

        self.gridLayout_4.addWidget(self.sdxlRefinerCheckpointCombo, 30, 1, 1, 2)

        self.label_3 = QLabel(self.parametersTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 17, 0, 1, 1)

        self.label_7 = QLabel(self.parametersTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 19, 0, 1, 1)

        self.label_4 = QLabel(self.parametersTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 18, 0, 1, 1)

        self.label_11 = QLabel(self.parametersTab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.cfgValue = QSpinBox(self.parametersTab)
        self.cfgValue.setObjectName(u"cfgValue")
        self.cfgValue.setMinimum(1)
        self.cfgValue.setMaximum(40)
        self.cfgValue.setValue(8)

        self.gridLayout_4.addWidget(self.cfgValue, 18, 1, 1, 1)

        self.batchValue = QSpinBox(self.parametersTab)
        self.batchValue.setObjectName(u"batchValue")
        self.batchValue.setMinimum(1)
        self.batchValue.setMaximum(64)
        self.batchValue.setValue(2)

        self.gridLayout_4.addWidget(self.batchValue, 17, 1, 1, 1)

        self.label = QLabel(self.parametersTab)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 15, 0, 1, 1)

        self.settingsTab.addTab(self.parametersTab, "")
        self.loraTab = QWidget()
        self.loraTab.setObjectName(u"loraTab")
        self.loraTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.loraTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_24 = QLabel(self.loraTab)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)

        self.loraStrengthSpin = QDoubleSpinBox(self.loraTab)
        self.loraStrengthSpin.setObjectName(u"loraStrengthSpin")
        self.loraStrengthSpin.setMaximum(2.000000000000000)
        self.loraStrengthSpin.setSingleStep(0.050000000000000)
        self.loraStrengthSpin.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.loraStrengthSpin, 4, 3, 1, 1)

        self.line_7 = QFrame(self.loraTab)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 2, 3, 1, 1)

        self.loraCheck = QCheckBox(self.loraTab)
        self.loraCheck.setObjectName(u"loraCheck")

        self.gridLayout_3.addWidget(self.loraCheck, 0, 0, 1, 1)

        self.loraClipStrengthSpin = QDoubleSpinBox(self.loraTab)
        self.loraClipStrengthSpin.setObjectName(u"loraClipStrengthSpin")
        self.loraClipStrengthSpin.setMaximum(2.000000000000000)
        self.loraClipStrengthSpin.setSingleStep(0.050000000000000)
        self.loraClipStrengthSpin.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.loraClipStrengthSpin, 5, 3, 1, 1)

        self.loraCombo = QComboBox(self.loraTab)
        self.loraCombo.setObjectName(u"loraCombo")

        self.gridLayout_3.addWidget(self.loraCombo, 1, 3, 1, 1)

        self.label_23 = QLabel(self.loraTab)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 4, 0, 1, 1)

        self.label_21 = QLabel(self.loraTab)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 5, 0, 1, 1)

        self.settingsTab.addTab(self.loraTab, "")
        self.modelsTab = QWidget()
        self.modelsTab.setObjectName(u"modelsTab")
        self.modelsTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.modelsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_19 = QLabel(self.modelsTab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)

        self.reloadModelsButton = QPushButton(self.modelsTab)
        self.reloadModelsButton.setObjectName(u"reloadModelsButton")

        self.gridLayout_2.addWidget(self.reloadModelsButton, 2, 0, 1, 1)

        self.comfyuiExtraFolderValue = QLineEdit(self.modelsTab)
        self.comfyuiExtraFolderValue.setObjectName(u"comfyuiExtraFolderValue")
        self.comfyuiExtraFolderValue.setReadOnly(True)

        self.gridLayout_2.addWidget(self.comfyuiExtraFolderValue, 1, 1, 1, 1)

        self.label_15 = QLabel(self.modelsTab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)

        self.comfyuiModelFolderSelect = QToolButton(self.modelsTab)
        self.comfyuiModelFolderSelect.setObjectName(u"comfyuiModelFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiModelFolderSelect, 0, 2, 1, 1)

        self.comfyuiExtraFolderSelect = QToolButton(self.modelsTab)
        self.comfyuiExtraFolderSelect.setObjectName(u"comfyuiExtraFolderSelect")

        self.gridLayout_2.addWidget(self.comfyuiExtraFolderSelect, 1, 2, 1, 1)

        self.comfyuiModelFolderValue = QLineEdit(self.modelsTab)
        self.comfyuiModelFolderValue.setObjectName(u"comfyuiModelFolderValue")
        self.comfyuiModelFolderValue.setReadOnly(True)

        self.gridLayout_2.addWidget(self.comfyuiModelFolderValue, 0, 1, 1, 1)

        self.settingsTab.addTab(self.modelsTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.keepImagesCheck = QCheckBox(self.tab)
        self.keepImagesCheck.setObjectName(u"keepImagesCheck")

        self.gridLayout_5.addWidget(self.keepImagesCheck, 0, 0, 1, 1)

        self.maxImagesSpin = QSpinBox(self.tab)
        self.maxImagesSpin.setObjectName(u"maxImagesSpin")
        self.maxImagesSpin.setMinimum(32)
        self.maxImagesSpin.setMaximum(128)

        self.gridLayout_5.addWidget(self.maxImagesSpin, 1, 1, 1, 1)

        self.settingsTab.addTab(self.tab, "")

        self.gridLayout.addWidget(self.settingsTab, 1, 0, 1, 1)

        QWidget.setTabOrder(self.useExternalVaeCheck, self.imgWidthValue)
        QWidget.setTabOrder(self.imgWidthValue, self.imgHeightValue)
        QWidget.setTabOrder(self.imgHeightValue, self.seedValue)
        QWidget.setTabOrder(self.seedValue, self.iterationsValue)
        QWidget.setTabOrder(self.iterationsValue, self.batchValue)
        QWidget.setTabOrder(self.batchValue, self.cfgValue)
        QWidget.setTabOrder(self.cfgValue, self.stepsValue)
        QWidget.setTabOrder(self.stepsValue, self.loraCheck)
        QWidget.setTabOrder(self.loraCheck, self.loraCombo)
        QWidget.setTabOrder(self.loraCombo, self.loraStrengthSpin)
        QWidget.setTabOrder(self.loraStrengthSpin, self.loraClipStrengthSpin)
        QWidget.setTabOrder(self.loraClipStrengthSpin, self.comfyuiModelFolderValue)
        QWidget.setTabOrder(self.comfyuiModelFolderValue, self.comfyuiModelFolderSelect)
        QWidget.setTabOrder(self.comfyuiModelFolderSelect, self.comfyuiExtraFolderValue)
        QWidget.setTabOrder(self.comfyuiExtraFolderValue, self.comfyuiExtraFolderSelect)
        QWidget.setTabOrder(self.comfyuiExtraFolderSelect, self.saveSettingsButton)

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
        self.label_9.setText(QCoreApplication.translate("SettingsDialog", u"Width:", None))
#if QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Use an external VAE instead of model's built-in VAE", None))
#endif // QT_CONFIG(tooltip)
        self.useExternalVaeCheck.setText(QCoreApplication.translate("SettingsDialog", u"Use external VAE:", None))
        self.label_10.setText(QCoreApplication.translate("SettingsDialog", u"Height:", None))
        self.label_6.setText(QCoreApplication.translate("SettingsDialog", u"Scheduler:", None))
#if QT_CONFIG(tooltip)
        self.sdxlRefinerStepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform with SDXL refiner", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.sdxlRefinerCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable refiner when using SDXL", None))
#endif // QT_CONFIG(tooltip)
        self.sdxlRefinerCheck.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Refiner", None))
#if QT_CONFIG(tooltip)
        self.modelUpscaleCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Upscale final image with upscale model", None))
#endif // QT_CONFIG(tooltip)
        self.modelUpscaleCheck.setText(QCoreApplication.translate("SettingsDialog", u"Upscale with model:", None))
#if QT_CONFIG(tooltip)
        self.stepsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of steps to perform when generating iamge", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.modelUpscaleCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Upscale model to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.clipSkipValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Set last layer of CLIP. -1 for normal", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("SettingsDialog", u"SDXL refiner steps:", None))
        self.label_13.setText(QCoreApplication.translate("SettingsDialog", u"SDXL Refiner model:", None))
        self.label_20.setText(QCoreApplication.translate("SettingsDialog", u"Iterations:", None))
        self.label_25.setText(QCoreApplication.translate("SettingsDialog", u"Clip skip:", None))
        self.schedulerValue.setItemText(0, QCoreApplication.translate("SettingsDialog", u"normal", None))
        self.schedulerValue.setItemText(1, QCoreApplication.translate("SettingsDialog", u"karras", None))
        self.schedulerValue.setItemText(2, QCoreApplication.translate("SettingsDialog", u"exponential", None))
        self.schedulerValue.setItemText(3, QCoreApplication.translate("SettingsDialog", u"simple", None))
        self.schedulerValue.setItemText(4, QCoreApplication.translate("SettingsDialog", u"ddim_uniform", None))

#if QT_CONFIG(tooltip)
        self.schedulerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise scheduler to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.imgWidthValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Width of the generated image", None))
#endif // QT_CONFIG(tooltip)
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
        self.samplerValue.setItemText(12, QCoreApplication.translate("SettingsDialog", u"dpmpp_3m_sde", None))
        self.samplerValue.setItemText(13, QCoreApplication.translate("SettingsDialog", u"dpmpp_3m_sde_gpu", None))
        self.samplerValue.setItemText(14, QCoreApplication.translate("SettingsDialog", u"ddim", None))
        self.samplerValue.setItemText(15, QCoreApplication.translate("SettingsDialog", u"uni_pc", None))
        self.samplerValue.setItemText(16, QCoreApplication.translate("SettingsDialog", u"uni_pc_bh2", None))

#if QT_CONFIG(tooltip)
        self.samplerValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Noise sampler to use", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.iterationsValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Number of iterations to perform", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SettingsDialog", u"Sampler:", None))
#if QT_CONFIG(tooltip)
        self.seedValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Seed to use. -1 for random", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.imgHeightValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Height of the generated image", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Batch size:", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialog", u"Steps:", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"CFG scale:", None))
        self.label_11.setText(QCoreApplication.translate("SettingsDialog", u"Model:", None))
#if QT_CONFIG(tooltip)
        self.cfgValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"CFG scale value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.batchValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"How many images to generate at once. More VRAM", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Seed:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.parametersTab), QCoreApplication.translate("SettingsDialog", u"Parameters", None))
        self.label_24.setText(QCoreApplication.translate("SettingsDialog", u"LoRA model:", None))
#if QT_CONFIG(tooltip)
        self.loraStrengthSpin.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the model strength of the LoRA", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loraCheck.setToolTip(QCoreApplication.translate("SettingsDialog", u"Enable a LoRA when generating images", None))
#endif // QT_CONFIG(tooltip)
        self.loraCheck.setText(QCoreApplication.translate("SettingsDialog", u"Enable LoRA", None))
#if QT_CONFIG(tooltip)
        self.loraClipStrengthSpin.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the clip strength of the LoRA", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.loraCombo.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select SD1/2 LoRA", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("SettingsDialog", u"LoRA model strength:", None))
        self.label_21.setText(QCoreApplication.translate("SettingsDialog", u"LoRA clip strength:", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.loraTab), QCoreApplication.translate("SettingsDialog", u"LoRA", None))
        self.label_19.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI extra checkpoints folder:", None))
#if QT_CONFIG(tooltip)
        self.reloadModelsButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Reload models", None))
#endif // QT_CONFIG(tooltip)
        self.reloadModelsButton.setText(QCoreApplication.translate("SettingsDialog", u"Reload", None))
#if QT_CONFIG(tooltip)
        self.comfyuiExtraFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to extra checkpoints folder, must be recognised by ComfyUI", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiExtraFolderValue.setText("")
        self.label_15.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI models folder: ", None))
#if QT_CONFIG(tooltip)
        self.comfyuiModelFolderSelect.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select the 'ComfyUI/models' folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiModelFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.comfyuiExtraFolderSelect.setToolTip(QCoreApplication.translate("SettingsDialog", u"Select a ComfyUI extra models folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiExtraFolderSelect.setText(QCoreApplication.translate("SettingsDialog", u"...", None))
#if QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setToolTip(QCoreApplication.translate("SettingsDialog", u"Path to the 'ComfyUI/models' folder", None))
#endif // QT_CONFIG(tooltip)
        self.comfyuiModelFolderValue.setText(QCoreApplication.translate("SettingsDialog", u"ComfyUI/models", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.modelsTab), QCoreApplication.translate("SettingsDialog", u"Paths", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Max images:", None))
        self.keepImagesCheck.setText(QCoreApplication.translate("SettingsDialog", u"Keep images in display", None))
        self.settingsTab.setTabText(self.settingsTab.indexOf(self.tab), QCoreApplication.translate("SettingsDialog", u"Preferences", None))
    # retranslateUi

