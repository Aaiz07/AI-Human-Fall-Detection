from ultralytics import YOLO


class PersonDetector:

    def __init__(self, model):

        self.model = model

    # -----------------------------------------

    def detect(self, frame):

        detections = []

        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            classes=[0],          # Person class
            verbose=False
        )

        if len(results) == 0:
            return detections

        result = results[0]

        if (
            result.boxes is None
            or result.keypoints is None
            or result.boxes.id is None
        ):
            return detections

        boxes = result.boxes.xyxy.cpu().numpy()

        ids = result.boxes.id.cpu().numpy().astype(int)

        keypoints = result.keypoints.xy.cpu().numpy()

        for box, person_id, kp in zip(boxes, ids, keypoints):

            detections.append({

                "id": person_id,

                "box": box,

                "keypoints": kp

            })

        return detections