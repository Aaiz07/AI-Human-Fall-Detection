class ImpactDetector:

    def __init__(self):

        self.previous_speed = {}

        self.impact_detected = {}

    # ----------------------------------
    # Initialize Person
    # ----------------------------------

    def initialize(self, person_id):

        if person_id not in self.previous_speed:

            self.previous_speed[person_id] = 0

            self.impact_detected[person_id] = False

    # ----------------------------------
    # Detect Impact
    # ----------------------------------

    def detect(
        self,
        person_id,
        vertical_speed,
        acceleration
    ):

        self.initialize(person_id)

        impact = False

        # Sudden fast downward movement

        if (

            vertical_speed > 30

            and

            acceleration > 8

        ):

            impact = True

        self.previous_speed[person_id] = vertical_speed

        self.impact_detected[person_id] = impact

        return impact

    # ----------------------------------
    # Get Impact Status
    # ----------------------------------

    def is_impact(
        self,
        person_id
    ):

        self.initialize(person_id)

        return self.impact_detected[person_id]

    # ----------------------------------
    # Reset
    # ----------------------------------

    def reset(
        self,
        person_id
    ):

        if person_id in self.previous_speed:

            del self.previous_speed[person_id]

        if person_id in self.impact_detected:

            del self.impact_detected[person_id]