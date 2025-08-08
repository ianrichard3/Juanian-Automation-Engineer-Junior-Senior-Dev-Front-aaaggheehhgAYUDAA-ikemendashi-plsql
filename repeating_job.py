import threading
import time
from screenshot import take_screenshot, take_webcam_screen_photo, take_webcam_photo

class RepeatingJob:
    def __init__(self, interval, func, *args, **kwargs):
        self.interval = float(interval)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._stop_evt = threading.Event()
        self._running = False
        self._thread = None

    def _run(self):
        # Espera interval; si _stop_evt se setea, sale
        while not self._stop_evt.wait(self.interval):
            self.func(*self.args, **self.kwargs)
        self._running = False

    def start(self):
        if self._running:
            return
        self._stop_evt.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        self._running = True

    def stop(self):
        if not self._running:
            return
        self._stop_evt.set()
        # Opcional: esperar a que termine
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=self.interval + 1)
        self._running = False

    def toggle(self):
        if self._running:
            self.stop()
        else:
            self.start()

    def is_running(self):
        return self._running
