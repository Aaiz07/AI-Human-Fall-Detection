from datetime import date


class Statistics:

    def __init__(self):

        self.total_people = set()

        self.total_falls = 0

        self.active_falls = set()

        self.today = date.today()

    # ------------------------------------

    def update_person(self, person_id):

        self.total_people.add(person_id)

    # ------------------------------------

    def register_fall(self, person_id):

        if person_id not in self.active_falls:

            self.active_falls.add(person_id)

            self.total_falls += 1

    # ------------------------------------

    def recover(self, person_id):

        if person_id in self.active_falls:

            self.active_falls.remove(person_id)

    # ------------------------------------

    def get_stats(self):

        return {

            "people": len(self.total_people),

            "falls": self.total_falls,

            "active": len(self.active_falls)

        }