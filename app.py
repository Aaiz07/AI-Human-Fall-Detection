import cv2
from ultralytics import YOLO

from detector import PersonDetector
from pose import BodyAnalyzer
from fall_detector import FallDetector

from logger import FallLogger
from dashboard import Dashboard
from alert import AlertSystem
from video_recorder import VideoRecorder

from config import *


# ---------------------------------------
# Load Model
# ---------------------------------------

model = YOLO(MODEL_PATH)

detector = PersonDetector(model)

analyzer = BodyAnalyzer()

fall_detector = FallDetector()

logger = FallLogger()

dashboard = Dashboard()

alert = AlertSystem()

recorder = VideoRecorder()

# ---------------------------------------
# Camera
# ---------------------------------------

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():

    print("Cannot open camera.")

    exit()

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
while True:

    ret, frame = cap.read()

    if not ret:

        break

    detections = detector.detect(frame)

    for detection in detections:

        person_id = detection["id"]

        box = detection["box"]

        keypoints = detection["keypoints"]

        analysis = analyzer.analyze(

            box,

            keypoints

        )

        result = fall_detector.detect(

            person_id,

            analysis

        )

        x1, y1, x2, y2 = map(int, box)

        color = (0, 255, 0)

        if result["fall"]:

            color = (0, 0, 255)

        elif result["state"] == "POSSIBLE_FALL":

            color = (0, 255, 255)

        cv2.rectangle(

            frame,

            (x1, y1),

            (x2, y2),

            color,

            2

        )
        cv2.putText(

            frame,

            f"ID : {person_id}",

            (x1, y1 - 70),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            color,

            2

        )

        cv2.putText(

            frame,

            f"State : {result['state']}",

            (x1, y1 - 45),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            color,

            2

        )

        cv2.putText(

            frame,

            f"Speed : {result['speed']:.1f}",

            (x1, y1 - 20),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            color,

            2

        )

        dashboard.update(frame, person_id, result)

        if result["fall"]:

            logger.log(person_id)

            alert.trigger()

            recorder.save(frame)

    cv2.imshow(

        WINDOW_NAME,

        frame

    )

    key = cv2.waitKey(1)

    if key == ord("q"):

        break

cap.release()

cv2.destroyAllWindows()