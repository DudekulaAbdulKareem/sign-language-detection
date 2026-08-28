# 🤟 Sign Language Detection

<p align="center">
  <strong>Real-Time Sign Language Detection using YOLO, OpenCV & Flask</strong>
</p>

<p align="center">
  A computer vision application that detects sign-language gestures through image uploads and real-time webcam interaction.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-purple)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?logo=flask)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

</p>

---

## 🎯 Project Highlights

- 🤖 **YOLO-powered** sign-language detection
- 📷 **Image upload** for gesture detection
- 🎥 **Live webcam** detection
- 🌐 **Flask-based** web application
- 🧠 Deep-learning computer vision model
- ⚡ Real-time prediction capability

---

## 🚀 Overview

This project uses a trained YOLO object detection model to recognize sign-language gestures through a Flask web application.

The system demonstrates how deep learning and computer vision can be combined with a web interface to create an accessible real-time sign-language detection application.

### Supported Signs

| Gesture | Class |
|---|---|
| 👋 | Hello |
| ❤️ | I Love You |
| ❌ | No |
| 🙏 | Thanks |
| 👍 | Yes |

---

## ✨ Features

- 🤖 YOLO-based sign-language detection
- 📷 Image upload interface
- 🎥 Real-time webcam detection
- 🌐 Flask web application
- 🧠 Deep-learning-based object detection
- 📊 Confidence-based predictions
- ⚡ Real-time computer vision processing
- 🎨 Clean and responsive user interface

---

## 📸 Application Preview

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 📤 Image Upload

![Upload Page](screenshots/upload.png)

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- YOLO
- Ultralytics

### Computer Vision

- OpenCV
- NumPy

### Web Development

- Flask
- HTML
- CSS

### Tools

- Git
- GitHub
- Antigravity

---

## 🧠 How It Works

```text
                    👤 User
                       │
             ┌─────────┴─────────┐
             │                   │
        📷 Image Upload      🎥 Webcam
             │                   │
             └─────────┬─────────┘
                       ↓
                🌐 Flask App
                       ↓
                🤖 YOLO Model
                       ↓
              🧠 Sign Detection
                       ↓
                📊 Prediction
'''

##📁 Project Structure
    sign-language-detection/
    │
    ├── app.py
    ├── run.py
    ├── best.pt
    ├── data.yaml
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    │
    ├── screenshots/
    │   ├── home.png
    │   └── upload.png
    │
    ├── static/
    └── templates/


---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DudekulaAbdulKareem/sign-language-detection.git

```

### 2. Navigate to the Project Directory

```bash
cd sign-language-detection
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
