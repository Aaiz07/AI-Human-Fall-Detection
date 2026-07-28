# ==========================================
# Camera
# ==========================================

CAMERA_ID = 0

WINDOW_NAME = "AI Human Fall Detection System"

# ==========================================
# YOLO Model
# ==========================================

MODEL_PATH = "models/yolo11n-pose.pt"

CONFIDENCE_THRESHOLD = 0.5

TRACKER_CONFIG = "bytetrack.yaml"

# ==========================================
# Body Analysis
# ==========================================

STANDING_RATIO = 1.40

SITTING_RATIO = 0.80

BODY_ANGLE_THRESHOLD = 60

# ==========================================
# Motion Analysis
# ==========================================

VERTICAL_SPEED_THRESHOLD = 20

HORIZONTAL_SPEED_THRESHOLD = 15

ACCELERATION_THRESHOLD = 5

IMPACT_SPEED_THRESHOLD = 30

IMPACT_ACCELERATION_THRESHOLD = 8

# ==========================================
# Fall Decision
# ==========================================

POSSIBLE_FALL_FRAMES = 5

GROUND_CONFIRM_FRAMES = 20

RECOVERY_FRAMES = 15

# ==========================================
# Motion History
# ==========================================

HISTORY_SIZE = 30

# ==========================================
# Recording
# ==========================================

RECORDING_FRAMES = 200

SCREENSHOT_FOLDER = "screenshots"

RECORDING_FOLDER = "recordings"

LOG_FOLDER = "logs"