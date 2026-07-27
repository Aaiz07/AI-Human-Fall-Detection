class FallDetector:

    def __init__(self):

        self.counter = {}
        self.alerted = set()

    def detect(self, person_id, analysis):

        ratio = analysis["ratio"]
        angle = analysis["angle"]

        if person_id not in self.counter:
            self.counter[person_id] = 0

        if ratio < 0.8 and angle > 60:
            self.counter[person_id] += 1
        else:
            self.counter[person_id] = 0

            if person_id in self.alerted:
                self.alerted.remove(person_id)

        if self.counter[person_id] >= 10:

            if person_id not in self.alerted:

                self.alerted.add(person_id)

                return True

        return False

    def recovered(self, person_id, analysis):

        ratio = analysis["ratio"]

        if ratio > 1.4:
            return True

        return False