import os
import winsound


class AlertSystem:

    def __init__(self):

        os.makedirs("screenshots", exist_ok=True)

    def alarm(self):

        winsound.Beep(1500, 500)