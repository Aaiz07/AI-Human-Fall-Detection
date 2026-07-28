class StateMachine:

    def __init__(self):

        self.states = {}

    # ----------------------------------------
    # Initialize Person
    # ----------------------------------------

    def initialize(self, person_id):

        if person_id not in self.states:

            self.states[person_id] = "STANDING"

    # ----------------------------------------
    # Get State
    # ----------------------------------------

    def get_state(self, person_id):

        self.initialize(person_id)

        return self.states[person_id]

    # ----------------------------------------
    # Set State
    # ----------------------------------------

    def set_state(self, person_id, state):

        self.initialize(person_id)

        self.states[person_id] = state

    # ----------------------------------------
    # Update State
    # ----------------------------------------

    def update(
        self,
        person_id,
        posture,
        vertical_speed,
        acceleration,
        ground_frames
    ):

        self.initialize(person_id)

        current_state = self.states[person_id]

        # ----------------------------------------
        # Standing
        # ----------------------------------------

        if posture == "Standing":

            self.states[person_id] = "STANDING"

            return self.states[person_id]

        # ----------------------------------------
        # Sitting / Bending
        # ----------------------------------------

        if posture == "Sitting":

            self.states[person_id] = "BENDING"

            return self.states[person_id]

        # ----------------------------------------
        # Lying
        # ----------------------------------------

        if posture == "Lying":

            # Fast downward motion
            if vertical_speed > 20 and acceleration > 5:

                self.states[person_id] = "POSSIBLE_FALL"

            # Stayed on ground
            if current_state == "POSSIBLE_FALL":

                if ground_frames >= 5:

                    self.states[person_id] = "ON_GROUND"

            # Confirmed
            if current_state == "ON_GROUND":

                if ground_frames >= 20:

                    self.states[person_id] = "FALL_CONFIRMED"

            return self.states[person_id]

        return self.states[person_id]

    # ----------------------------------------
    # Recovery
    # ----------------------------------------

    def recover(self, person_id, posture):

        self.initialize(person_id)

        if posture == "Standing":

            if self.states[person_id] == "FALL_CONFIRMED":

                self.states[person_id] = "RECOVERED"

                return True

        return False

    # ----------------------------------------
    # Reset
    # ----------------------------------------

    def reset(self, person_id):

        if person_id in self.states:

            del self.states[person_id]