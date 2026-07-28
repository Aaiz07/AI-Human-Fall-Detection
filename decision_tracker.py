from collections import deque


class DecisionTracker:

    def __init__(self, history_size=30):

        self.history_size = history_size

        self.people = {}

    # ----------------------------------------
    # Create person if not exists
    # ----------------------------------------

    def initialize(self, person_id):

        if person_id not in self.people:

            self.people[person_id] = {

                "state": "STANDING",

                "history": deque(maxlen=self.history_size),

                "center_history": deque(maxlen=self.history_size),

                "speed_history": deque(maxlen=self.history_size),

                "acceleration_history": deque(maxlen=self.history_size),

                "confidence": 0,

                "ground_frames": 0,

                "possible_frames": 0,

                "standing_frames": 0,

                "bending_frames": 0,

                "recovered": False,

                "fall_detected": False,

                "last_speed": 0,

                "last_center": None
            }

    # ----------------------------------------
    # Update Current Frame
    # ----------------------------------------

    def update(self,
               person_id,
               posture,
               center,
               speed,
               acceleration):

        self.initialize(person_id)

        person = self.people[person_id]

        person["history"].append(posture)

        person["center_history"].append(center)

        person["speed_history"].append(speed)

        person["acceleration_history"].append(acceleration)

        person["last_center"] = center

        person["last_speed"] = speed

    # ----------------------------------------
    # State
    # ----------------------------------------

    def set_state(self, person_id, state):

        self.initialize(person_id)

        self.people[person_id]["state"] = state

    def get_state(self, person_id):

        self.initialize(person_id)

        return self.people[person_id]["state"]

    # ----------------------------------------
    # Counters
    # ----------------------------------------

    def increment_ground(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["ground_frames"] += 1

    def reset_ground(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["ground_frames"] = 0

    def get_ground_frames(self, person_id):

        self.initialize(person_id)

        return self.people[person_id]["ground_frames"]

    def increment_possible(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["possible_frames"] += 1

    def reset_possible(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["possible_frames"] = 0

    def get_possible_frames(self, person_id):

        self.initialize(person_id)

        return self.people[person_id]["possible_frames"]

    # ----------------------------------------
    # Standing Counter
    # ----------------------------------------

    def increment_standing(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["standing_frames"] += 1

    def reset_standing(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["standing_frames"] = 0

    # ----------------------------------------
    # Bending Counter
    # ----------------------------------------

    def increment_bending(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["bending_frames"] += 1

    def reset_bending(self, person_id):

        self.initialize(person_id)

        self.people[person_id]["bending_frames"] = 0

    # ----------------------------------------
    # Confidence
    # ----------------------------------------

    def set_confidence(self,
                       person_id,
                       confidence):

        self.initialize(person_id)

        self.people[person_id]["confidence"] = confidence

    def get_confidence(self,
                       person_id):

        self.initialize(person_id)

        return self.people[person_id]["confidence"]

    # ----------------------------------------
    # Fall Flag
    # ----------------------------------------

    def set_fall(self,
                 person_id,
                 status):

        self.initialize(person_id)

        self.people[person_id]["fall_detected"] = status

    def is_fall(self,
                person_id):

        self.initialize(person_id)

        return self.people[person_id]["fall_detected"]

    # ----------------------------------------
    # Recovery
    # ----------------------------------------

    def set_recovered(self,
                      person_id,
                      status):

        self.initialize(person_id)

        self.people[person_id]["recovered"] = status

    def is_recovered(self,
                     person_id):

        self.initialize(person_id)

        return self.people[person_id]["recovered"]

    # ----------------------------------------
    # Reset Person
    # ----------------------------------------

    def reset(self,
              person_id):

        if person_id in self.people:

            del self.people[person_id]