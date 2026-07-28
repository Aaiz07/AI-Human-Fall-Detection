import math


class MotionAnalyzer:

    def __init__(self):

        self.previous_center = {}

        self.previous_speed = {}

    # ----------------------------------

    def initialize(self, person_id):

        if person_id not in self.previous_center:

            self.previous_center[person_id] = None

            self.previous_speed[person_id] = 0

    # ----------------------------------

    def analyze(self, person_id, center):

        self.initialize(person_id)

        previous = self.previous_center[person_id]

        if previous is None:

            self.previous_center[person_id] = center

            return {

                "dx": 0,

                "dy": 0,

                "speed": 0,

                "vertical_speed": 0,

                "horizontal_speed": 0,

                "acceleration": 0

            }

        px, py = previous

        cx, cy = center

        dx = cx - px

        dy = cy - py

        speed = math.sqrt(dx**2 + dy**2)

        acceleration = speed - self.previous_speed[person_id]

        self.previous_speed[person_id] = speed

        self.previous_center[person_id] = center

        return {

            "dx": round(dx,2),

            "dy": round(dy,2),

            "speed": round(speed,2),

            "vertical_speed": round(dy,2),

            "horizontal_speed": round(dx,2),

            "acceleration": round(acceleration,2)

        }

    # ----------------------------------

    def reset(self, person_id):

        if person_id in self.previous_center:

            del self.previous_center[person_id]

        if person_id in self.previous_speed:

            del self.previous_speed[person_id]