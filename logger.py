from datetime import datetime
import os

from config import LOG_FOLDER


class FallLogger:

    def __init__(self):

        os.makedirs(LOG_FOLDER, exist_ok=True)

        self.log_file = os.path.join(

            LOG_FOLDER,

            "fall_log.csv"

        )

        if not os.path.exists(self.log_file):

            with open(self.log_file, "w") as f:

                f.write(

                    "Time,PersonID,State\n"

                )

    # --------------------------------

    def log(self, person_id):

        now = datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

        with open(

            self.log_file,

            "a"

        ) as f:

            f.write(

                f"{now},{person_id},FALL_CONFIRMED\n"

            )