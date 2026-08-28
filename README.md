# 🤟 Sign Language Detection

> Real-time sign language detection using YOLO, OpenCV, and Flask.

A computer vision application that detects and recognizes hand signs through image input and real-time webcam detection.

---

## 🚀 Overview

This project uses a trained YOLO object detection model to recognize common sign-language gestures.

The application provides a simple web interface built with Flask, allowing users to upload images or use their webcam for real-time detection.

### Supported Signs

| Sign | Detection |
|---|---|
| 👋 | Hello |
| ❤️ | I Love You |
| ❌ | No |
| 🙏 | Thanks |
| 👍 | Yes |

---

## ✨ Features

- 🤖 YOLO-based sign-language detection
- 📷 Image upload detection
- 🎥 Real-time webcam detection
- 🌐 Flask web application
- 📊 Confidence-based predictions
- ⚡ Real-time computer vision processing
- 🎨 Clean and responsive web interface

---

## 🛠️ Tech Stack

### Programming

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

### Development Tools

- Git
- GitHub
- VS Code / Antigravity

---

## 🧠 How It Works

```text
User
  │
  ├── Upload Image
  │
  └── Webcam
        │
        ▼
   Flask Application
        │
        ▼
   YOLO Detection Model
        │
        ▼
  Sign Classification
        │
        ▼
 Detection Result