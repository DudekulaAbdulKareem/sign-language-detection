# <p align="center"> <h1 align="center">🤟 Sign Language Detection</h1> </p> <p align="center"> <strong>Real-Time Sign Language Detection using YOLO, OpenCV & Flask</strong> </p>

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

```


### ⚙️ Installation

### Prerequisites
- Before running the project, make sure you have:
    - Python 3.x installed
    - Git installed
    - A working webcam for live detection   

You can verify Python is installed by running:

    ```bash
    python --version
    ```
### 1. Clone the Repository
```bash
git clone https://github.com/DudekulaAbdulKareem/sign-language-detection.git
```

### 2. Navigate to the Project Directory

```bash
cd sign-language-detection
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify the Model File
Make sure the trained YOLO model file is present in the project folder: 

    ```bash
    best.pt
    ```

### 5. Start the Application
 ```bash
    python app.py
   ```

### 6. Run the Application:
- After starting the Flask server, open the URL shown in the terminal.
 - Usually:

    ```bash
        Start the Flask application:

            python app.py

        Then open the application in your browser:

            http://127.0.0.1:5000
    ```

### 7. Using Live Detection
- For live sign-language detection:
    - Open the Live Detection page.
    - Allow browser access to your webcam when prompted.
    - Make sure your webcam is connected and working.
    - Position your hand clearly in front of the camera.

### ⚠️ Troubleshooting
### Python is not recognized

  -  Make sure Python is installed and added to your system PATH.

### Dependencies are missing
  - Run:
     ```bash
     pip install -r requirements.txt
     ```
     again from the project directory.

### Webcam is not working
   Check that your webcam is connected and that your browser has permission to access it.

### Model file not found
   Make sure best.pt is present in the project directory.

### Model file is missing

  -  Make sure the best.pt file is present in the project folder.

### 🎬 Demo
    The application provides two ways to interact with the sign-language detection system:

    📤 Image Upload — Upload an image and detect the sign-language gesture.
    🎥 Live Detection — Use your webcam for real-time sign-language detection.

### 💡 Use Cases
   - 🤝 Accessibility technology
   - 🗣️ Sign-language recognition
   - 👨‍💻 Human-computer interaction
   - 🤖 Real-time object detection
   - 🎓 Computer vision learning
   - 💻 Assistive technology

### 🔮 Future Improvements
   - Add more sign-language gestures
   - Improve model accuracy
   - Support complete sign-language sentences
   - Add text-to-speech functionality
   - Deploy the application to the cloud
   - Improve mobile responsiveness
   - Add multilingual support
   -  Optimize real-time detection performance

### 📌 Project Status
Status: Completed Portfolio Project 🚀

   - The current version supports sign-language gesture detection through image upload and real-time webcam interaction.

### 👨‍💻 Author
 * Abdul Kareem

   - Computer Science / Technology Enthusiast passionate about Python, Machine Learning, Data Analytics, and Software Development.

   - GitHub:https://github.com/DudekulaAbdulKareem   

### 📄 License
   - This project is available for educational and portfolio purposes.    