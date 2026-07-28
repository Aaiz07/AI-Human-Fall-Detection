import math

from config import *


class BodyAnalyzer:

    def __init__(self):

        pass

    # ----------------------------------

    def distance(self,p1,p2):

        return math.sqrt(

            (p1[0]-p2[0])**2 +

            (p1[1]-p2[1])**2

        )

    # ----------------------------------

    def calculate_angle(self,a,b):

        dx = a[0]-b[0]

        dy = a[1]-b[1]

        return abs(

            math.degrees(

                math.atan2(dx,dy)

            )

        )

    # ----------------------------------

    def analyze(self,box,keypoints):

        x1,y1,x2,y2 = box

        width = x2-x1

        height = y2-y1

        ratio = height/width if width>0 else 0

        center_x = int((x1+x2)/2)

        center_y = int((y1+y2)/2)

        left_shoulder = keypoints[5]

        right_shoulder = keypoints[6]

        left_hip = keypoints[11]

        right_hip = keypoints[12]

        left_knee = keypoints[13]

        right_knee = keypoints[14]

        left_ankle = keypoints[15]

        right_ankle = keypoints[16]

        shoulder = (

            (left_shoulder[0]+right_shoulder[0])/2,

            (left_shoulder[1]+right_shoulder[1])/2

        )

        hip = (

            (left_hip[0]+right_hip[0])/2,

            (left_hip[1]+right_hip[1])/2

        )

        knee = (

            (left_knee[0]+right_knee[0])/2,

            (left_knee[1]+right_knee[1])/2

        )

        ankle = (

            (left_ankle[0]+right_ankle[0])/2,

            (left_ankle[1]+right_ankle[1])/2

        )

        torso_angle = self.calculate_angle(

            shoulder,

            hip

        )

        leg_angle = self.calculate_angle(

            hip,

            ankle

        )

        hip_angle = abs(

            torso_angle-leg_angle

        )

        torso_length = self.distance(

            shoulder,

            hip

        )

        leg_length = self.distance(

            hip,

            ankle

        )

        body_length = torso_length + leg_length

        if ratio > STANDING_RATIO:

            posture = "Standing"

        elif ratio > SITTING_RATIO:

            posture = "Sitting"

        else:

            posture = "Lying"

        return {

            "width": int(width),

            "height": int(height),

            "ratio": round(ratio,2),

            "center": (

                center_x,

                center_y

            ),

            "angle": round(

                torso_angle,

                2

            ),

            "posture": posture,

            "shoulder": shoulder,

            "hip": hip,

            "knee": knee,

            "ankle": ankle,

            "torso_angle": round(

                torso_angle,

                2

            ),

            "leg_angle": round(

                leg_angle,

                2

            ),

            "hip_angle": round(

                hip_angle,

                2

            ),

            "body_length": round(

                body_length,

                2

            )

        }