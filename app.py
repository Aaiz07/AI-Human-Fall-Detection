import cv2
import time
from datetime import datetime

from detector import PersonDetector
from pose import BodyAnalyzer
from fall_detector import FallDetector
from logger import FallLogger
from alert import AlertSystem
from video_recorder import VideoRecorder
from dashboard import Dashboard
from config import *

# ==============================
# Initialize Modules
# ==============================

detector = PersonDetector(
    MODEL_PATH,
    CONFIDENCE_THRESHOLD
)

analyzer = BodyAnalyzer()

fall_detector = FallDetector()

logger = FallLogger()

alert = AlertSystem()

recorder = VideoRecorder()

dashboard = Dashboard()

# ==============================
# Variables
# ==============================

fall_count = 0
people_count = 0

recording = False
record_frames = 0

camera_status = "Active"

# ==============================
# Open Camera
# ==============================

cap = cv2.VideoCapture(CAMERA_ID)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

prev_time = time.time()

# ==============================
# Main Loop
# ==============================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = detector.track(frame, TRACKER_CONFIG)

    annotated_frame = results[0].plot()

    people_count = 0

    if (
        results[0].boxes is not None
        and results[0].boxes.id is not None
        and results[0].keypoints is not None
    ):

        ids = results[0].boxes.id.cpu().numpy().astype(int)
        boxes = results[0].boxes.xyxy.cpu().numpy()
        keypoints = results[0].keypoints.xy.cpu().numpy()

        people_count = len(ids)

        for track_id, box, person_keypoints in zip(
            ids,
            boxes,
            keypoints,
        ):

            analysis = analyzer.analyze(
                box,
                person_keypoints
            )

            fall_detected = fall_detector.detect(
                track_id,
                analysis
            )

            # --------------------------
            # Start Video Recording
            # --------------------------

            if fall_detected and not recording:

                recorder.start(frame)

                recording = True

                record_frames = 200

                fall_count += 1

            x1, y1, x2, y2 = map(int, box)

            # --------------------------
            # Person Status
            # --------------------------

            if fall_detected:

                status = "FALL DETECTED"

                color = (0, 0, 255)

            else:

                status = analysis["posture"]

                color = (0, 255, 0)

            # --------------------------
            # Draw Track ID
            # --------------------------

            cv2.putText(
                annotated_frame,
                f"ID: {track_id}",
                (x1, y1 - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2,
            )

            # --------------------------
            # Draw Status
            # --------------------------

            cv2.putText(
                annotated_frame,
                status,
                (x1, y1 - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2,
            )

            # --------------------------
            # Draw Center
            # --------------------------

            cx, cy = analysis["center"]

            cv2.circle(
                annotated_frame,
                (cx, cy),
                5,
                (255, 0, 0),
                -1,
            )
                        # --------------------------
            # Print Information
            # --------------------------

            print("-" * 60)
            print(f"Person ID : {track_id}")
            print(f"Width     : {analysis['width']}")
            print(f"Height    : {analysis['height']}")
            print(f"Ratio     : {analysis['ratio']}")
            print(f"Angle     : {analysis['angle']}")
            print(f"Center    : {analysis['center']}")
            print(f"Posture   : {analysis['posture']}")

            # --------------------------
            # Fall Event
            # --------------------------

            if fall_detected:

                print("=" * 60)
                print(f"🚨 FALL DETECTED - Person ID {track_id}")
                print("=" * 60)

                alert.alarm()

                logger.log(track_id)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                filename = (
                    f"screenshots/fall_{track_id}_{timestamp}.jpg"
                )

                cv2.imwrite(filename, annotated_frame)

                print(f"Screenshot Saved : {filename}")

        # --------------------------
        # Draw Keypoints
        # --------------------------

        for person in keypoints:

            for x, y in person:

                if x > 0 and y > 0:

                    cv2.circle(
                        annotated_frame,
                        (int(x), int(y)),
                        3,
                        (0, 0, 255),
                        -1,
                    )

    # --------------------------
    # Video Recording
    # --------------------------

    if recording:

        recorder.write(frame)

        record_frames -= 1

        if record_frames <= 0:

            recorder.stop()

            recording = False

    # --------------------------
    # FPS
    # --------------------------

    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # --------------------------
    # Dashboard Status
    # --------------------------

    dashboard_status = "Monitoring"

    if recording:
        dashboard_status = "Recording"

    annotated_frame = dashboard.draw(
        annotated_frame,
        people_count,
        fall_count,
        int(fps),
        dashboard_status,
    )

    # --------------------------
    # Camera Status
    # --------------------------

    cv2.putText(
        annotated_frame,
        f"Camera : {camera_status}",
        (20, 205),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
    )

    # --------------------------
    # Total Falls
    # --------------------------

    cv2.putText(
        annotated_frame,
        f"Total Falls : {fall_count}",
        (20, 230),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 255),
        2,
    )

    # --------------------------
    # Show Window
    # --------------------------

    cv2.imshow(
        WINDOW_NAME,
        annotated_frame,
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# ==============================
# Cleanup
# ==============================

if recording:
    recorder.stop()

cap.release()

cv2.destroyAllWindows()