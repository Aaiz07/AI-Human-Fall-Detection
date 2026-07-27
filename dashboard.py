import cv2


class Dashboard:

    def draw(
        self,
        frame,
        people,
        falls,
        fps,
        status
    ):

        cv2.rectangle(
            frame,
            (10, 10),
            (330, 180),
            (40, 40, 40),
            -1,
        )

        cv2.rectangle(
            frame,
            (10, 10),
            (330, 180),
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            "AI HUMAN FALL DETECTION",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"People : {people}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Falls  : {falls}",
            (20, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2,
        )

        cv2.putText(
            frame,
            f"FPS    : {fps}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Status : {status}",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2,
        )

        return frame