# Hand Gesture Volume Control 🎵✋

This project lets you **control your system volume using hand gestures** with the help of **MediaPipe** and **OpenCV**. By detecting the distance between your **thumb** and **index finger**, the volume is smoothly adjusted in real-time.

---

## 🚀 Features

* Real-time **hand tracking** using MediaPipe
* Gesture-based **volume control** (Thumb ↔ Index Finger distance)
* **Smooth transition** in volume change (avoids sudden jumps)
* Works with your **system’s default audio device** using **pycaw**

---

## 🛠️ Tech Stack

* **Python 3.11**
* [MediaPipe](https://developers.google.com/mediapipe) – Hand Tracking
* [OpenCV](https://opencv.org/) – Computer Vision
* [PyCaw](https://github.com/AndreMiras/pycaw) – System Volume Control
* **comtypes & ctypes** – Windows Audio Interface

---

## 📦 Installation

Clone the repo and install the dependencies:

```bash
git clone https://github.com/your-username/hand-gesture-volume-control.git
cd hand-gesture-volume-control

pip install opencv-python mediapipe pycaw comtypes
```

---

## ▶️ Usage

Run the script:

```bash
python gesture_volume.py
```

* Show your hand to the camera.
* Move your **thumb** and **index finger** closer → Volume decreases 🔉
* Move them farther apart → Volume increases 🔊
* Press **`q`** to quit.

---

## 📷 Demo (Example Output)

```
Volume: 63%
```
<img width="1519" height="849" alt="image" src="https://github.com/user-attachments/assets/077b7915-feb1-4366-8369-8137e36687bd" />


---

## ⚠️ Notes

* Works on **Windows only** (since PyCaw is Windows-specific).
* Requires a **webcam**.
* Best performance with **Python 3.11** and good lighting.

---

## 🔮 Future Improvements

* Add **gesture shortcuts** (mute/unmute, play/pause).
* Support for **Linux/Mac** with alternative audio libraries.

---

## 👨‍💻 Author

Made with ❤️ using Python, MediaPipe, and OpenCV.

---
