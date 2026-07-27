import math


class BodyAnalyzer:

    def __init__(self):
        pass

    def analyze(self, box, keypoints):

        x1, y1, x2, y2 = box

        width = x2 - x1
        height = y2 - y1

        ratio = height / width if width > 0 else 0

        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        angle = 0

        try:
            left_shoulder = keypoints[5]
            right_shoulder = keypoints[6]

            left_hip = keypoints[11]
            right_hip = keypoints[12]

            shoulder_x = (left_shoulder[0] + right_shoulder[0]) / 2
            shoulder_y = (left_shoulder[1] + right_shoulder[1]) / 2

            hip_x = (left_hip[0] + right_hip[0]) / 2
            hip_y = (left_hip[1] + right_hip[1]) / 2

            dx = shoulder_x - hip_x
            dy = shoulder_y - hip_y

            angle = abs(math.degrees(math.atan2(dx, dy)))

        except Exception:
            angle = 0

        if ratio > 1.4:
            posture = "Standing"

        elif ratio > 0.8:
            posture = "Sitting"

        else:
            posture = "Lying"

        return {
            "width": int(width),
            "height": int(height),
            "ratio": round(ratio, 2),
            "center": (center_x, center_y),
            "angle": round(angle, 2),
            "posture": posture,
        }