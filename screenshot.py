import pyautogui
import os
from datetime import datetime
import cv2
import numpy as np


def take_screenshot(output_dir, screenshot_prefix="screenshot"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{output_dir}/{screenshot_prefix}-{timestamp}.png")


def take_webcam_photo(output_dir, photo_prefix="photo"):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{output_dir}/{photo_prefix}-{timestamp}.png"

    cap = cv2.VideoCapture(0)  # 0 es el índice de la webcam principal

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Foto guardada en {filename}")
    else:
        print("No se pudo capturar la imagen.")

    cap.release()

def take_webcam_screen_photo(output_dir, photo_prefix="photo"):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{output_dir}/{photo_prefix}-{timestamp}.png"

    # Capturar pantalla
    screenshot = pyautogui.screenshot()
    screen_img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Capturar webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    ret, webcam_frame = cap.read()
    cap.release()

    if not ret:
        print("No se pudo capturar la imagen de la cámara.")
        return

    # Redimensionar la imagen de la cámara (PiP size)
    pip_width = 320
    pip_height = 240
    webcam_small = cv2.resize(webcam_frame, (pip_width, pip_height))

    # Coordenadas para superponer (esquina superior derecha)
    x_offset = screen_img.shape[1] - pip_width - 20  # 20px de margen derecho
    y_offset = 20  # 20px desde arriba

    # Superponer webcam sobre screenshot
    screen_img[y_offset:y_offset+pip_height, x_offset:x_offset+pip_width] = webcam_small

    # Guardar imagen final
    cv2.imwrite(filename, screen_img)
    print(f"Foto combinada guardada en {filename}")
