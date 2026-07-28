import cv2


class Dashboard:

    def __init__(self):

        pass

    # -------------------------------

    def update(self, frame, person_id, result):

        text = [

            f"ID : {person_id}",

            f"State : {result['state']}",

            f"Posture : {result['posture']}",

            f"Speed : {result['speed']:.1f}",

            f"Acceleration : {result['acceleration']:.1f}",

            f"Impact : {result['impact']}"

        ]

        x = 20

        y = 30

        for t in text:

            cv2.putText(

                frame,

                t,

                (x, y),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.6,

                (255,255,255),

                2

            )

            y += 25
            