import time


class FallTimer:

    def __init__(self):

        self.start_times = {}

    # ------------------------------

    def start(self, person_id):

        if person_id not in self.start_times:

            self.start_times[person_id] = time.time()

    # ------------------------------

    def stop(self, person_id):

        if person_id in self.start_times:

            del self.start_times[person_id]

    # ------------------------------

    def duration(self, person_id):

        if person_id not in self.start_times:

            return 0

        return round(

            time.time()

            -

            self.start_times[person_id],

            1

        )