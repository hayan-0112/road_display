from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSignal, Qt, QPoint
import os
from datetime import datetime

# UI 파일 로드
form_class = uic.loadUiType("ImgDataWindow.ui")[0]

class ImgDataWindow(QMainWindow, form_class):
    image_selected = pyqtSignal(str)  # 이미지 경로 문자열을 방출하도록 시그널 정의

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.image_selected.connect(self.display_image)
        self.scale_factor = 1.0
        self.pixmap = None  # QPixmap
        self.offset = QPoint(0, 0)
        self.dragging = False

    def init_ui(self):
        self.setFixedSize(562, 483)
        self.road_image2.setFixedSize(520, 330)
        self.road_image2.setMouseTracking(True)

    def display_image(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.scale_factor = 1.0
        self.fit_to_label()
        self.display_image_info(image_path)

    def fit_to_label(self):
        if self.pixmap:
            label_size = self.road_image2.size()
            scaled_pixmap = self.pixmap.scaled(
                label_size,
                Qt.IgnoreAspectRatio,  # IgnoreAspectRatio를 사용하여 이미지를 레이블 크기에 맞춤
                Qt.SmoothTransformation
            )
            self.road_image2.setPixmap(scaled_pixmap)
            self.road_image2.setAlignment(Qt.AlignCenter)  # 이미지 가운데 정렬
            self.offset = QPoint(0, 0)

    def display_image_info(self, image_path):
        modification_time = os.path.getmtime(image_path)
        formatted_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
        self.road2_data.setText(f"{formatted_time}")

    def update_image(self):
        if self.pixmap:
            # 배율을 적용
            scaled_pixmap = self.pixmap.scaled(
                self.road_image2.size() * self.scale_factor,
                Qt.IgnoreAspectRatio,  # IgnoreAspectRatio를 사용하여 이미지를 레이블 크기에 맞춤
                Qt.SmoothTransformation
            )
            # 이미지를 QPixmap에서 QImage로 변환
            image = scaled_pixmap.toImage()
            self.road_image2.setPixmap(QPixmap.fromImage(image))

    def wheelEvent(self, event):
        if self.pixmap:
            if event.angleDelta().y() > 0:
                self.scale_factor *= 1.1
            else:
                self.scale_factor *= 0.9

            if self.scale_factor < 1.0:
                self.scale_factor = 1.0

            self.update_image()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.scale_factor > 1.0:
            self.dragging = True
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging and self.scale_factor > 1.0:
            delta = event.pos() - self.drag_start_position
            self.offset += delta
            self.drag_start_position = event.pos()
            self.move_image()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def move_image(self):
        if self.pixmap:
            # 이미지를 이동시킬 때 사용하는 오프셋 계산
            label_size = self.road_image2.size()
            scaled_pixmap = self.pixmap.scaled(
                self.pixmap.size() * self.scale_factor,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            image = scaled_pixmap.toImage()

            # 이동한 오프셋을 사용하여 이미지를 잘라서 표시
            cropped_image = image.copy(
                -self.offset.x(), -self.offset.y(),
                min(label_size.width(), image.width() + self.offset.x()),
                min(label_size.height(), image.height() + self.offset.y())
            )
            self.road_image2.setPixmap(QPixmap.fromImage(cropped_image))