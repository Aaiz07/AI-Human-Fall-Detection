import csv
from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.filename = "logs/daily_report.csv"

    def save(self, person_id, result):

        now = datetime.now()

        with open(self.filename, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([

                now.strftime("%Y-%m-%d"),

                now.strftime("%H:%M:%S"),

                person_id,

                result["state"],

                result["posture"],

                result["speed"],

                result["acceleration"]

            ])
            if state == "STANDING":

                 color = (0,255,0)

            elif state == "POSSIBLE_FALL":

                color = (0,255,255)

            elif state == "ON_GROUND":

                color = (255,0,0)

            elif state == "FALL_CONFIRMED":

               color = (0,0,255)

            else:

              color = (255,255,255)
              import os

              folders = [

                   "logs",

                   "screenshots",

                   "recordings",

                   "models"

            ]

for folder in folders:

    os.makedirs(

        folder,

        exist_ok=True

    )
    from datetime import datetime

filename = datetime.now().strftime(

    "screenshots/fall_%Y%m%d_%H%M%S.jpg"

)

cv2.imwrite(

    filename,

    frame

)
