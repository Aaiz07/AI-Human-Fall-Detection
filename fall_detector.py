from collections import deque

from config import *

from motion_analyzer import MotionAnalyzer


class FallDetector:

    def __init__(self):

        self.motion = MotionAnalyzer()

        # Store data separately for each tracked person
        self.people = {}

    # -------------------------------------------------

    def initialize(self, person_id):

        if person_id not in self.people:

            self.people[person_id] = {

                # Current state
                "state": "STANDING",

                # Current detection result
                "fall": False,

                # Motion history
                "history": deque(maxlen=HISTORY_SIZE),

                # Counters
                "possible_frames": 0,
                "ground_frames": 0,
                "recovery_frames": 0,

                # Impact
                "impact": False,

                # Last motion values
                "speed": 0,
                "vertical_speed": 0,
                "horizontal_speed": 0,
                "acceleration": 0,

                # Last posture
                "posture": "Standing",

                # Confidence helper
                "lying_frames": 0

            }

    # -------------------------------------------------

    def detect(self, person_id, analysis):

        self.initialize(person_id)

        person = self.people[person_id]

        motion = self.motion.analyze(

            person_id,

            analysis["center"]

        )

        person["speed"] = motion["speed"]

        person["vertical_speed"] = motion["vertical_speed"]

        person["horizontal_speed"] = motion["horizontal_speed"]

        person["acceleration"] = motion["acceleration"]

        person["posture"] = analysis["posture"]

        person["history"].append(

            analysis["center"]

        )
                # -----------------------------------------
        # Impact Detection
        # -----------------------------------------

        if (

            abs(person["vertical_speed"]) >

            IMPACT_SPEED_THRESHOLD

            and

            abs(person["acceleration"]) >

            IMPACT_ACCELERATION_THRESHOLD

        ):

            person["impact"] = True

        else:

            person["impact"] = False

        # -----------------------------------------
        # Standing
        # -----------------------------------------

        if analysis["posture"] == "Standing":

            person["state"] = "STANDING"

            person["possible_frames"] = 0

            person["ground_frames"] = 0

            person["recovery_frames"] = 0

            person["lying_frames"] = 0

            person["fall"] = False

        # -----------------------------------------
        # Sitting / Bending
        # -----------------------------------------

        elif analysis["posture"] == "Sitting":

            person["state"] = "BENDING"

            person["possible_frames"] = 0

            person["ground_frames"] = 0

            person["lying_frames"] = 0

        # -----------------------------------------
        # Lying
        # -----------------------------------------

        else:

            person["lying_frames"] += 1
                        # Fast movement + impact

            if person["impact"]:

                person["possible_frames"] += 1

            else:

                person["possible_frames"] = max(

                    0,

                    person["possible_frames"] - 1

                )

            if (

                person["possible_frames"]

                >= POSSIBLE_FALL_FRAMES

            ):

                person["state"] = "POSSIBLE_FALL"

            # Ground confirmation

            if person["lying_frames"] > 0:

                person["ground_frames"] += 1

            if (

                person["ground_frames"]

                >= GROUND_CONFIRM_FRAMES

            ):

                person["state"] = "ON_GROUND"
                            # Confirm fall

            if (

                person["state"] == "ON_GROUND"

                and

                person["impact"]

            ):

                person["state"] = "FALL_CONFIRMED"

                person["fall"] = True

        # -----------------------------------------
        # Recovery
        # -----------------------------------------

        if (

            person["fall"]

            and

            analysis["posture"] == "Standing"

        ):

            person["recovery_frames"] += 1

            if (

                person["recovery_frames"]

                >= RECOVERY_FRAMES

            ):

                person["state"] = "RECOVERED"

                person["fall"] = False

        return person

    # -------------------------------------------------

    def is_fall(self, person_id):

        if person_id not in self.people:

            return False

        return self.people[person_id]["fall"]

    # -------------------------------------------------

    def get_state(self, person_id):

        if person_id not in self.people:

            return "UNKNOWN"

        return self.people[person_id]["state"]

    # -------------------------------------------------

    def reset(self, person_id):

        if person_id in self.people:

            del self.people[person_id]

        self.motion.reset(person_id)