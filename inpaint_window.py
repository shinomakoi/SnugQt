from pathlib import Path

from PySide6.QtCore import QPoint, QSize
from PySide6.QtGui import Qt, QIcon, QImage, QColor, QAction, QColor, QPen, QPainter
from PySide6.QtWidgets import QMainWindow

APP_ICON = Path("assets/appicon.png")


class InpaintMaskEditor(QMainWindow):
    def __init__(self, inpaint_source, inpaint_mask):
        super().__init__()

        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.inpaint_source = inpaint_source
        self.img_mask_path = inpaint_mask

        self.setWindowTitle("SnugQt - Inpaint mask editor")

        self.setMaximumHeight(self.inpaint_source.height() / 1.6)
        self.setMaximumWidth(self.inpaint_source.width() / 1.6)
        self.setMinimumHeight(self.inpaint_source.height() / 1.6)
        self.setMinimumWidth(self.inpaint_source.width() / 1.6)

        # creating image object
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.out_img = QImage(self.size(), QImage.Format_ARGB32)

        # Load inpaint source
        self.image = self.inpaint_source

        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 32
        # default color
        self.brushColor = QColor(0, 0, 0, 255)

        # QPoint object to track the point
        self.lastPoint = QPoint()

        # creating menu bar
        mainMenu = self.menuBar()

        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")

        b_size = mainMenu.addMenu("Brush Size")

        inpaintAction = QAction("Save", self)

        fileMenu.addAction(inpaintAction)

        inpaintAction.triggered.connect(self.save_mask)
        # saveAction.triggered.connect(self.save)

        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + C")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(lambda: self.clear())

        pix_6 = QAction("6px", self)
        # adding this action to the brush size
        b_size.addAction(pix_6)
        # adding method to this
        pix_6.triggered.connect(self.Pixel_6)

        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_24 = QAction("24px", self)
        b_size.addAction(pix_24)
        pix_24.triggered.connect(self.Pixel_24)

        pix_32 = QAction("32px", self)
        b_size.addAction(pix_32)
        pix_32.triggered.connect(self.Pixel_32)

        pix_48 = QAction("48px", self)
        b_size.addAction(pix_48)
        pix_48.triggered.connect(self.Pixel_48)

        pix_72 = QAction("72px", self)
        b_size.addAction(pix_72)
        pix_72.triggered.connect(self.Pixel_72)

        pix_96 = QAction("96px", self)
        b_size.addAction(pix_96)
        pix_96.triggered.connect(self.Pixel_96)

    # method for checking mouse cicks
    def mousePressEvent(self, event):
        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.scenePosition()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):
        if (event.buttons() and Qt.LeftButton) and self.drawing:
            # creating painter object
            painter = QPainter(self.out_img)

            # set the pen of the painter
            painter.setPen(
                QPen(
                    self.brushColor,
                    self.brushSize,
                    Qt.SolidLine,
                    Qt.RoundCap,
                    Qt.RoundJoin,
                )
            )

            painter.drawLine(self.lastPoint, event.scenePosition())

            # change the last point
            self.lastPoint = event.scenePosition()
            # update
            self.update()

    # method for mouse left button release
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        canvasPainter.drawImage(self.rect(), self.out_img, self.out_img.rect())

    def save_mask(self):
        mask = self.out_img.createMaskFromColor(0, Qt.MaskInColor)
        self.image.setAlphaChannel(mask)
        self.image.save(str(self.img_mask_path))
        print("--- Inpaint mask saved")
        return self.image

    def clear(self):
        # make the whole canvas white
        self.out_img.fill(Qt.transparent)
        self.update()

    def Pixel_6(self):
        self.brushSize = 6

    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_24(self):
        self.brushSize = 24

    def Pixel_32(self):
        self.brushSize = 32

    def Pixel_48(self):
        self.brushSize = 48

    def Pixel_72(self):
        self.brushSize = 72

    def Pixel_96(self):
        self.brushSize = 96

    def blackColor(self):
        self.brushColor = QColor(Qt.black)
