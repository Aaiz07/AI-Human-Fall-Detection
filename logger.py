import csv
import os
from datetime import datetime


class FallLogger:

    def __init__(self):

        self.file = "logs/fall_logs.csv"

        os.makedirs("logs", exist_ok=True)

        if not os.path.exists(self.file):

            with open(self.file, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "Timestamp",
                    "Person ID",
                    "Status"
                ])

    def log(self, person_id):

        with open(self.file, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                person_id,
                "Fall Detected"
            ])