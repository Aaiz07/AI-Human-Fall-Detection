import winsound


class AlertSystem:

    def __init__(self):

        self.active = False

    # -------------------------------

    def trigger(self):

        if self.active:

            return

        self.active = True

        winsound.Beep(

            1000,

            500

        )

        self.active = False