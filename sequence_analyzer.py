from motion_analyzer import MotionAnalyzer
from decision_tracker import DecisionTracker
from impact_detector import ImpactDetector
from sequence_analyzer import SequenceAnalyzer
from state_machine import StateMachine

from config import *


class FallDetector:

    def __init__(self):

        self.motion = MotionAnalyzer()

        self.tracker = DecisionTracker(
            history_size=HISTORY_SIZE
        )

        self.impact = ImpactDetector()

        self.sequence = SequenceAnalyzer(
            history_size=HISTORY_SIZE
        )

        self.state_machine = StateMachine()

    # =====================================
    # Main Detection Function
    # =====================================

    def detect(self, person_id, analysis):

        posture = analysis["posture"]
        ratio = analysis["ratio"]
        angle = analysis["angle"]
        center = analysis["center"]

        # -----------------------------------
        # Motion Analysis
        # -----------------------------------

        motion = self.motion.analyze(
            person_id,
            center
        )

        vertical_speed = motion["vertical_speed"]

        acceleration = motion["acceleration"]

        # -----------------------------------
        # Save History
        # -----------------------------------

        self.tracker.update(

            person_id,

            posture,

            center,

            vertical_speed,

            acceleration

        )

        # -----------------------------------
        # Impact Detection
        # -----------------------------------

        impact = self.impact.detect(

            person_id,

            vertical_speed,

            acceleration

        )

        # -----------------------------------
        # Standing
        # -----------------------------------

        if posture == "Standing":

            self.state_machine.set_state(
                person_id,
                "STANDING"
            )

            self.sequence.update(
                person_id,
                "STANDING"
            )

            self.tracker.reset_ground(
                person_id
            )

            self.tracker.reset_possible(
                person_id
            )

            self.tracker.set_fall(
                person_id,
                False
            )

            return False

        # -----------------------------------
        # Sitting
        # -----------------------------------

        if posture == "Sitting":

            self.state_machine.set_state(
                person_id,
                "BENDING"
            )

            self.sequence.update(
                person_id,
                "BENDING"
            )

            return False

        # -----------------------------------
        # Lying
        # -----------------------------------

        if posture == "Lying":

            if impact:

                self.tracker.increment_possible(
                    person_id
                )

            else:

                self.tracker.reset_possible(
                    person_id
                )

            possible = self.tracker.get_possible_frames(
                person_id
            )
                        # -----------------------------------
            # Possible Fall
            # -----------------------------------

            if possible >= POSSIBLE_FALL_FRAMES:

                self.state_machine.set_state(
                    person_id,
                    "POSSIBLE_FALL"
                )

                self.sequence.update(
                    person_id,
                    "POSSIBLE_FALL"
                )

                self.tracker.increment_ground(
                    person_id
                )

            ground = self.tracker.get_ground_frames(
                person_id
            )

            # -----------------------------------
            # On Ground
            # -----------------------------------

            if ground >= GROUND_CONFIRM_FRAMES:

                self.state_machine.set_state(
                    person_id,
                    "ON_GROUND"
                )

                self.sequence.update(
                    person_id,
                    "ON_GROUND"
                )

            current_state = self.state_machine.get_state(
                person_id
            )

            # -----------------------------------
            # Sequence Verification
            # -----------------------------------

            valid_sequence = self.sequence.detect_fall_sequence(
                person_id
            )

            # -----------------------------------
            # Final Decision
            # -----------------------------------

            if (

                current_state == "ON_GROUND"

                and

                valid_sequence

            ):

                self.state_machine.set_state(

                    person_id,

                    "FALL_CONFIRMED"

                )

                self.sequence.update(

                    person_id,

                    "FALL_CONFIRMED"

                )

                if not self.tracker.is_fall(
                    person_id
                ):

                    self.tracker.set_fall(
                        person_id,
                        True
                    )

                    return True

            return False

        return False

    # =====================================
    # Recovery
    # =====================================

    def recovered(
        self,
        person_id,
        analysis
    ):

        posture = analysis["posture"]

        if self.state_machine.recover(
            person_id,
            posture
        ):

            self.tracker.set_fall(
                person_id,
                False
            )

            self.tracker.set_recovered(
                person_id,
                True
            )

            self.tracker.reset_ground(
                person_id
            )

            self.tracker.reset_possible(
                person_id
            )

            self.motion.reset(
                person_id
            )

            self.impact.reset(
                person_id
            )

            self.sequence.reset(
                person_id
            )

            return True

        return False

    # =====================================
    # Current State
    # =====================================

    def get_state(
        self,
        person_id
    ):

        return self.state_machine.get_state(
            person_id
        )

    # =====================================
    # Motion Information
    # =====================================

    def get_motion(
        self,
        person_id
    ):

        self.motion.initialize(
            person_id
        )

        return {

            "center": self.motion.previous_centers.get(
                person_id
            ),

            "speed": self.motion.previous_speeds.get(
                person_id
            )

        }

    # =====================================
    # Reset
    # =====================================

    def reset(
        self,
        person_id
    ):

        self.motion.reset(
            person_id
        )

        self.impact.reset(
            person_id
        )

        self.sequence.reset(
            person_id
        )

        self.tracker.reset(
            person_id
        )

        self.state_machine.reset(
            person_id
        )