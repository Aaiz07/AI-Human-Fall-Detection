import cv2
import os
from datetime import datetime

from config import RECORDING_FOLDER


class VideoRecorder:

    def __init__(self):

        os.makedirs(

            RECORDING_FOLDER,

            exist_ok=True

        )

    # -------------------------------

    def save(self, frame):

        filename = datetime.now().strftime(

            "%Y%m%d_%H%M%S.jpg"

        )

        path = os.path.join(

            RECORDING_FOLDER,

            filename

        )

        cv2.imwrite(

            path,

            frame

        )