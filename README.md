# Multimodal Attendance & Engagement Agent

An AI-powered, privacy-preserving classroom intelligence system. The system integrates computer vision, audio activity detection, and local decision-support logic to automate sustained attendance tracking, monitor engagement trends, and generate real-time teaching adjustments.

## 📌 Core Modules
- **Sustained Presence Attendance:** Tracks student presence over configurable intervals to prevent false positives from brief appearances.
- **Multimodal Engagement Dynamics:** Evaluates head pose estimation, gaze direction, and visual attention indicators.
- **Audio Activity Sensing:** Observes classroom dialogue distribution to evaluate discussion vs. lecture balance.
- **Contextual Teaching Coach:** Generates practical suggestions for educators to modify pacing or introduce activities when attention dips occur.

## 🛠️ Tech Stack
- **Language:** Python
- **Vision & Multimodal:** OpenCV, MediaPipe
- **Analytics & Dashboard:** Streamlit, Pandas, NumPy
- **Deployment:** 100% Offline & Edge Capable

## 📂 Project Structure
```text
multimodal-attendance-engagement-agent/
├── requirements.txt
├── README.md
└── src/
    ├── app.py
    ├── attendance_tracker.py
    ├── audio_monitor.py
    ├── engagement_analyzer.py
    └── suggestion_agent.py
