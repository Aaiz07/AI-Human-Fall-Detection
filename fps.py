import time


class FPSCounter:

    def __init__(self):

        self.prev = time.time()

        self.fps = 0

    # -------------------------------

    def update(self):

        now = time.time()

        diff = now - self.prev

        self.prev = now

        if diff > 0:

            self.fps = 1 / diff

        return round(self.fps, 1)