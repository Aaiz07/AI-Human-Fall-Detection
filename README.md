# 🚨 AI Human Fall Detection System

An AI-powered real-time Human Fall Detection System developed using **Python**, **OpenCV**, **Ultralytics YOLO11 Pose**, and **ByteTrack**. The system detects human falls in live video, tracks multiple people, and automatically records incidents with screenshots, videos, alarms, and logs.

---

## 📌 Project Overview

This project monitors people through a webcam or video stream and detects fall events in real time. When a fall is confirmed, the system:

- 🚨 Detects the fall
- 🔊 Triggers an alarm
- 📸 Captures a screenshot
- 🎥 Records the event as a video
- 📝 Saves the event in a CSV log
- 📊 Displays a live dashboard

---

## ✨ Features

- ✅ Real-Time Human Detection
- ✅ YOLO11 Pose Estimation
- ✅ Multi-Person Tracking using ByteTrack
- ✅ Human Pose Analysis
- ✅ AI-Based Fall Detection
- ✅ Live Dashboard
- ✅ FPS Counter
- ✅ People Counter
- ✅ Fall Counter
- ✅ Automatic Alarm
- ✅ Screenshot Capture
- ✅ Video Recording
- ✅ CSV Event Logging

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| OpenCV | Video processing and visualization |
| Ultralytics YOLO11 Pose | Human pose estimation |
| ByteTrack | Multi-person tracking |
| NumPy | Numerical operations |
| Pandas | CSV logging and data handling |

---

## 🏗️ Project Structure

```text
fall-detection/
│
├── app.py
├── detector.py
├── pose.py
├── fall_detector.py
├── dashboard.py
├── logger.py
├── alert.py
├── video_recorder.py
├── config.py
├── requirements.txt
├── README.md
│
├── models/
├── logs/
├── screenshots/
└── videos/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Aaiz07/AI-Human-Fall-Detection.git
```

Go to the project folder:

```bash
cd AI-Human-Fall-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python app.py
```

Press **Q** to quit.

---

## 🔄 Workflow

```text
Camera
   │
   ▼
OpenCV
   │
   ▼
YOLO11 Pose Detection
   │
   ▼
ByteTrack Tracking
   │
   ▼
Body Analysis
   │
   ▼
Fall Detection Algorithm
   │
   ▼
──────────────────────────────
Dashboard
Alarm
Screenshot
Video Recording
CSV Logging
──────────────────────────────
```

---

## 📂 Output

When a fall is detected, the system automatically:

- Saves a screenshot in `screenshots/`
- Records a video in `videos/`
- Logs the event in `logs/fall_logs.csv`
- Displays an alert on the dashboard
- Plays an alarm sound

---

## 🚀 Future Improvements

- Email/SMS alerts
- Cloud database integration
- Web dashboard
- Mobile notifications
- Raspberry Pi deployment
- Night vision camera support

---

## 👨‍💻 Author

**Aaiz Tariq**

GitHub: https://github.com/Aaiz07

---

## ⭐ If you found this project useful, consider giving it a star!