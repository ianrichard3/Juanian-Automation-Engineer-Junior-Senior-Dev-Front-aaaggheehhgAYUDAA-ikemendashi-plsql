import threading
import time
from screenshot import take_screenshot , take_webcam_screen_photo , take_webcam_photo
from repeating_job import RepeatingJob

def start_listener(time_interval_seconds: float, callback_function, *args, **kwargs) -> None:
    def thread_job():
        while True:
            time.sleep(time_interval_seconds)
            callback_function(*args, **kwargs)

    hilo = threading.Thread(target=thread_job, daemon=True)
    hilo.start()






# job = RepeatingJob(5, take_screenshot, output_dir="paper")
# job.start()

# try:
#     while True:
#         print(f"Programa principal | running={job.is_running()}")
#         time.sleep(2)
#         # Ejemplo: alternar cada 10s
#         # if ...: job.toggle()
# except KeyboardInterrupt:
#     job.stop()

