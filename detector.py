from ultralytics import YOLO


class PersonDetector:

    def __init__(self, model_path, confidence=0.5):

        self.model = YOLO(model_path)

        self.confidence = confidence

    def track(self, frame, tracker):

        results = self.model.track(
            source=frame,
            tracker=tracker,
            persist=True,
            conf=self.confidence,
            verbose=False,
        )

        return results