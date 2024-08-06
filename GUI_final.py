import sys
import cv2
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QImage
from PyQt5.QtCore import QTimer
import os
import torch
import pathlib
import time
import mysql.connector
from mysql.connector import Error
from pathlib import Path
from datetime import datetime
import numpy as np
from ImgDataWindow import ImgDataWindow

# 경로 수정
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# YOLOv5 모델 로드
model_path = r"C:\Users\301-16\PycharmProjects\projectGUI\best.pt"
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)  # custom 모델 로드


# MySQL 데이터베이스 연결
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="192.168.31.198",  # MySQL 서버 IP 주소
            port=3306,  # MySQL 서버 포트
            user="user",  # 새로 생성한 사용자 이름
            password="0000",  # 새로 생성한 사용자 비밀번호
            database="road"  # 연결할 데이터베이스 이름
        )
        if connection.is_connected():
            print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection()

# UI 파일 로드
form_class = uic.loadUiType("interface.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.update_list()
        self.image_list.clicked.connect(self.display_image)
        self.imgDataBtn.clicked.connect(self.img_btn_func)
        self.Btn_video.clicked.connect(self.video_play)
        self.Btn_WebCAM.clicked.connect(self.webcam_play)
        self.img_data_window = None
        self.selected_image_path = None

        # OpenCV VideoCapture 객체 초기화
        self.cap = None  # 비디오 캡쳐 객체를 초기화하지 않음

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30ms마다 프레임 업데이트

        # 캡쳐 시간 초기화
        self.last_capture_time = 0
        self.color_difference = 0

        # 캡처된 이미지 저장 경로 설정
        self.capture_folder = Path('captured_images')
        self.capture_folder.mkdir(exist_ok=True)
        self.notice_timer = QTimer(self)
        self.notice_timer.timeout.connect(self.hide_notice_label)

        # 프레임 카운터 초기화
        self.frame_counter = 0

    def hide_notice_label(self):
        self.notice.setVisible(False)
        self.notice_timer.stop()
    def init_ui(self):
        self.setFixedSize(920, 600)
        self.cam_display.setFixedSize(710, 430)

    def update_list(self):
        model = QStandardItemModel()

        cur = connection.cursor()
        cur.execute('SELECT name FROM road_data;')
        result = cur.fetchall()

        for row in result:
            image_file = row[0]
            item = QStandardItem(image_file)
            model.appendRow(item)
        self.image_list.setModel(model)

    def display_image(self, index):
        item = self.image_list.model().itemFromIndex(index)
        image_name = item.text()

        cur = connection.cursor()
        cur.execute("SELECT img FROM road_data WHERE name = %s", (image_name,))
        result = cur.fetchone()

        if result:
            image_data = result[0]
            image_path = f"temp_{image_name}.jpg"
            with open(image_path, 'wb') as file:
                file.write(image_data)

            self.selected_image_path = image_path
            print(f"Main Window: Displaying image {image_path}")

            if os.path.exists(image_path):
                print(f"Image path exists: {image_path}")
                pixmap = QPixmap(image_path)
                self.road_image.setPixmap(pixmap)
                self.road_image.setScaledContents(True)
            else:
                print(f"Error: Image file {image_path} does not exist.")

            if self.img_data_window and self.img_data_window.isVisible():
                print(f"Main Window: Emitting signal with path {image_path}")
                self.img_data_window.image_selected.emit(image_path)

    def img_btn_func(self):
        if not self.img_data_window:
            self.img_data_window = ImgDataWindow()
            self.img_data_window.image_selected.connect(self.img_data_window.display_image)

        self.img_data_window.show()

        if self.selected_image_path:
            self.img_data_window.image_selected.emit(self.selected_image_path)

    def video_play(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Video File")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov *.mkv)")
        file_dialog.setDirectory(r"C:\Users\301-16\PycharmProjects\projectGUI\video_file")
        self.color_difference = 88
        if file_dialog.exec_():
            video_path = file_dialog.selectedFiles()[0]
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(video_path)
            if not self.cap.isOpened():
                print(f"Error: Could not open video file {video_path}.")
            else:
                print(f"Playing video file {video_path}.")

    def webcam_play(self):
        self.color_difference = 190
        if self.cap:
            self.cap.release()
        self.cap = cv2.VideoCapture("http://192.168.31.176:81/stream")
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
        else:
            print("Accessing webcam.")

    def update_frame(self):
        self.frame_counter += 1
        if self.frame_counter % 2 == 0:
            if self.cap:
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, (640, 480))

                    # YOLOv5 모델을 사용한 객체 탐지
                    results = model(frame)
                    detections = results.xyxy[0].cpu().numpy()

                    original_frame = frame.copy()
                    detected = False
                    for *box, conf, cls in detections:
                        if conf >= 0.60:
                            x1, y1, x2, y2 = map(int, box)
                            cropped_frame = original_frame[y1:y2, x1:x2].copy()

                            mask = self.process_image(cropped_frame)
                            if self.is_inner_area_erased(cropped_frame, mask, threshold=self.color_difference):
                                current_time = time.time()
                                if current_time - self.last_capture_time > 3:  # 3초 동안 캡처 금지
                                    timestamp_str = datetime.fromtimestamp(current_time).strftime('%Y%m%d_%H%M%S')
                                    full_frame_path = self.capture_folder / f'full_frame_{timestamp_str}.png'
                                    cv2.imwrite(str(full_frame_path), original_frame)

                                    capture_image_path = self.capture_folder / f'capture_{timestamp_str}.png'
                                    cv2.imwrite(str(capture_image_path), cropped_frame)

                                    # 내부 영역 저장
                                    inner_image_path = self.capture_folder / f'inner_{timestamp_str}.png'
                                    cv2.imwrite(str(inner_image_path), cropped_frame[mask == 255])

                                    # 외부 영역 저장
                                    outer_image = cropped_frame.copy()
                                    outer_image[mask == 255] = 0
                                    outer_image_path = self.capture_folder / f'outer_{timestamp_str}.png'
                                    cv2.imwrite(str(outer_image_path), outer_image)

                                    # 데이터베이스에 저장
                                    self.capture_frame(original_frame, timestamp_str)
                                    self.notice.setVisible(True)
                                    self.notice.setText(f"{timestamp_str} 캡쳐가 저장되었습니다.")
                                    self.notice_timer.start(2000)
                                    print(f"{capture_image_path}: 내부가 지워졌습니다. 전체 프레임도 저장되었습니다.")
                                    self.last_capture_time = current_time
                                break

                    for *box, conf, cls in detections:
                        if conf >= 0.65:
                            x1, y1, x2, y2 = map(int, box)
                            label = f"{model.names[int(cls)]} {conf:.2f}"
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

                    height, width, channel = frame.shape
                    step = channel * width
                    qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
                    self.cam_display.setPixmap(QPixmap.fromImage(qImg))
                    self.cam_display.setScaledContents(True)

    def capture_frame(self, frame, timestamp_str):
        capture_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = f"capture_{timestamp_str}.jpg"

        # 프레임을 RGB에서 BGR로 변환하여 저장
        _, buffer = cv2.imencode('.jpg', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
        image_data = buffer.tobytes()
        print(f"Captured: {filename}")

        # MySQL에 이미지 정보 저장
        self.save_to_database(filename, capture_time, image_data)

        # 이미지 파일 리스트 업데이트
        self.update_list()

    def save_to_database(self, filename, capture_time, image_data):
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO road_data (name, date, img) VALUES (%s, %s, %s)"
            val = (filename, capture_time, image_data)
            cursor.execute(sql, val)
            connection.commit()
            print(f"Record inserted successfully into table")
        except mysql.connector.Error as error:
            print(f"Failed to insert record into table: {error}")

    def closeEvent(self, event):
        if self.cap:
            self.cap.release()
        event.accept()

    # 이미지 처리 함수 정의
    def process_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)
        return mask

    # 내부와 외부 색상을 비교하여 지워졌는지 확인하는 함수 정의
    def is_inner_area_erased(self, image, mask, threshold=200):
        inner_pixels = image[mask == 255]
        if len(inner_pixels) == 0:
            inner_rgb_means = np.array([0, 0, 0])
        else:
            inner_rgb_means = np.mean(inner_pixels, axis=0)
        outer_pixels = image[mask == 0]
        if len(outer_pixels) == 0:
            outer_rgb_means = np.array([0, 0, 0])
        else:
            outer_rgb_means = np.mean(outer_pixels, axis=0)
        color_difference = np.linalg.norm(inner_rgb_means - outer_rgb_means)
        self.label_6.setText(f"[{inner_rgb_means[0]:.0f}, {inner_rgb_means[1]:.0f}, {inner_rgb_means[2]:.0f}]")
        self.label_7.setText(f"[{outer_rgb_means[0]:.0f}, {outer_rgb_means[1]:.0f}, {outer_rgb_means[2]:.0f}]")
        self.label_8.setText(f"[{color_difference:.0f}]")

        print(f"내부 RGB 평균값: {inner_rgb_means}, 외부 RGB 평균값: {outer_rgb_means}, 색상 차이: {color_difference}")
        if color_difference <= self.color_difference:
            return True
        else:
            print(f"색상 차이 {color_difference}이(가) 범위를 벗어나 무시되었습니다.")
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
