# SafeSense AI: Intelligent Safety Companion for Women

**Event:** #75HER Challenge Hackathon 2026

SafeSense AI is an **AI-powered personal safety system designed specifically for women** to detect potential danger situations using **audio and motion intelligence** from a smartphone. The system monitors the surrounding environment for **distress signals such as loud screams and sudden violent movements** and automatically alerts trusted contacts when a possible emergency is detected.

The platform combines **sound anomaly detection, motion analysis, and AI-based reasoning** to provide a proactive safety layer. If the system detects a **distress scream combined with sudden movement**, it triggers an emergency alert with the user's location.

SafeSense AI focuses on **preventing harm and enabling faster help**, especially in situations where a victim cannot manually call for assistance.

---

# 🎯 Project Overview

SafeSense AI addresses a critical real-world problem:

Women often **cannot access help quickly during threatening situations** such as harassment, assault attempts, accidents, or unsafe environments.

In many cases:

- The victim cannot unlock the phone
- The victim cannot make a call
- The victim cannot manually send an SOS

SafeSense AI solves this by **automatically detecting distress signals** using AI.

The system provides:

- Real-time **scream detection**
- **Sudden motion / jerk detection**
- **False-positive reduction logic**
- **Automatic emergency alerts**
- **Trusted contact notification**
- **Location sharing during emergency**

This project demonstrates an **AI-assisted safety system** combining:

- Audio intelligence
- Motion anomaly detection
- Real-time alert automation
- Secure API architecture

Built as a **hackathon prototype**, but designed with a **scalable architecture suitable for real-world deployment**.

---

# 🎥 Demo Video (YouTube)

Watch the complete demo of **SafeSense AI – Intelligent Safety Companion for Women**

**SafeSense AI Demo Video**  
▶️ Click to Play

---

# 🏗️ System Architecture

## Three-Tier Architecture

| Layer | Description |
|------|-------------|
| Presentation Layer | Mobile or web interface |
| Application Layer | FastAPI backend handling detection logic |
| AI Layer | Scream detection + motion anomaly detection |

---

## AI Processing Flow

Microphone Audio  
⬇  
Scream Detection Model  
⬇  
Scream Duration Verification  
⬇  
Motion / Jerk Detection  
⬇  
Emergency Decision Engine  
⬇  
Alert System  
⬇  
Send Notification to Trusted Contacts

This creates a **multi-signal safety verification system** to reduce false alarms.

---

# 🚀 Technology Stack

## Backend

| Component | Technology |
|----------|------------|
| API Framework | FastAPI |
| Audio Detection | Python ML models |
| Motion Detection | Accelerometer data |
| Location | GPS APIs |
| Environment | Python 3.11 |
| API Docs | Swagger (OpenAPI) |

---

## Frontend

| Component | Technology |
|----------|------------|
| Interface | Prototype mobile/web app |
| Sensors | Microphone + Accelerometer |
| Alerts | SMS / Notification |
| Target Users | Women needing personal safety support |

---

# 🧠 AI Detection Pipeline

## Audio Intelligence

The system continuously listens for **high-intensity scream patterns** using audio classification models.

Detection includes:

- Loudness threshold detection
- Frequency pattern analysis
- Distress scream classification

To reduce false alarms:

A scream must last **at least 10 seconds** before being considered valid.

---

## Motion Intelligence

The phone’s **accelerometer sensor** detects sudden abnormal movements such as:

- Violent jerks
- Sudden drops
- Forced movement patterns

These signals help detect **possible struggle or danger situations**.

---

## Emergency Trigger Logic

SafeSense AI uses **multi-signal verification**.

Alert is triggered only if:

```
Scream Duration ≥ 10 seconds
AND
Sudden Motion / Jerk Detected
```

This helps prevent alerts caused by:

- Loud environments
- Normal shouting
- Accidental phone movements

---

# 📊 Key Safety Features

SafeSense AI provides:

- Automatic distress detection
- AI-based scream recognition
- Motion anomaly detection
- Trusted contact alert system
- GPS location sharing
- False-positive reduction mechanisms

The system acts as a **silent guardian** for users.

---

# 🔬 Testing & Evaluation

Evaluation was performed using **simulated emergency scenarios**, including:

- Loud scream detection tests
- Sudden movement simulations
- False-positive testing

Results showed:

- Reliable scream detection
- Effective motion anomaly recognition
- Reduced false alarms

This validates SafeSense AI as a **practical real-time safety assistant**.

---

# 🚀 Deployment Architecture

## Current Status

Hackathon prototype implementation:

- Local development environment
- Fully functional backend APIs
- Sensor simulation support

---

## Scalable by Design

The system can be extended to support:

- Mobile apps (Android / iOS)
- Wearable safety devices
- Smartwatch emergency detection
- Cloud-based monitoring systems

---

# 📂 Project Structure

```
SafeSense-AI/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── scream_detector.py
│   │   │   ├── motion_detector.py
│   │   │   ├── timer_manager.py
│   │   │   └── alert_service.py
│   │   ├── main.py
│   │   └── .gitignore
│
├── frontend/
│   └── app.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# 🔌 API Endpoint

### POST /detect_emergency

**Input**

- Audio stream
- Motion sensor data

**Output**

```json
{
  "scream_detected": true,
  "motion_detected": true,
  "emergency_triggered": true,
  "location": "User GPS location",
  "alert_sent": true
}
```

---

# ⚙️ Local Installation & Usage

## 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/safesense-backend.git
cd safesense-backend
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate:

Linux / Mac

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Environment Variables

Create `.env` file:

```
PORT=8000
ALERT_API_KEY=your_alert_service_key
```

---

## 5️⃣ Run Backend

```
uvicorn app.main:app --reload
```

API Base URL:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

# 🔐 Security Notes

- `.env` file is excluded via `.gitignore`
- No personal data is stored
- Detection processing is **stateless**
- Alerts are sent only to **trusted contacts**

---

# 🎯 Key Achievements

- AI-driven women's safety assistant
- Real-time distress detection
- Multi-signal verification system
- Automatic emergency alerts
- FastAPI scalable backend
- Hackathon-ready prototype
- Real-world social impact

---

# 🔮 Future Enhancements

Potential improvements:

- Mobile app
- Smartwatch integration
- AI scream recognition model training
- Offline detection capability
- Police emergency integration
- Safety monitoring dashboard

---

# 👥 Team

| Name | Role | GitHub |
|-----|-----|------|
| Kashmala Saddiqui | Backend integration  | https://github.com/kashmalaasif |
| Moneka Meghwar | Frontend integration | https://github.com/mmoneka11 |
| Umaima Rizwan | Documentation lead | https://github.com/ |

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🤝 Contributing

We welcome contributions. Please open issues or submit pull requests.

---

⭐ **Support this project:** If you find this project useful, please star the repository.

---

✨ **Built with ❤️ to improve women’s safety using AI**
