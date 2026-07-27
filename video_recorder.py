import cv2
import os
from datetime import datetime


class VideoRecorder:

    def __init__(self):

        os.makedirs("videos", exist_ok=True)

        self.writer = None

    def start(self, frame):

        filename = datetime.now().strftime(
            "videos/fall_%Y%m%d_%H%M%S.mp4"
        )

        h, w = frame.shape[:2]

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            20,
            (w, h),
        )

    def write(self, frame):

        if self.writer is not None:
            self.writer.write(frame)

    def stop(self):

        if self.writer is not None:

            self.writer.release()

            self.writer = None
            