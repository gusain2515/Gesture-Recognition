# Real-Time Hand Gesture Recognition

This project implements a **real-time hand gesture recognition system** using **OpenCV** and **MediaPipe**.  
The system can recognize static hand gestures such as **Open Palm, Fist, Peace Sign (V-sign), and Thumbs Up** through live webcam input.

---

## 🚀 Technology Justification

### OpenCV
- **Open Source Computer Vision Library**, widely used for computer vision tasks.  
- Provides robust, high-performance tools for:
  - Handling live video streams (`cv2.VideoCapture`)  
  - Image manipulation  
  - Overlaying results on video (`cv2.putText`)  

### MediaPipe
- **Cross-platform, open-source framework from Google** for building ML pipelines.  
- **Hands Solution** detects and tracks **21 hand landmarks in real-time** with high efficiency.  
- Optimized for **low-latency performance**, perfect for real-time gesture recognition.  
- Eliminates the need to train custom models from scratch.

**🔗 Combination of OpenCV (video handling) and MediaPipe (hand landmark detection) ensures high accuracy and real-time performance.**

---

## ✋ Gesture Recognition Logic

The system uses the **21 landmarks** provided by MediaPipe Hands.  
Finger state (extended/curled) is determined by comparing the **tip (y-coordinate)** with the **base MCP joint (y-coordinate)**.

- **Open Palm**  
  - All fingers extended  
  - Tips above (lower y) than MCP joints  

- **Fist**  
  - All fingers curled  
  - Tips below (higher y) than MCP joints  

- **Peace Sign (V-sign)**  
  - Index & Middle fingers extended  
  - Ring & Pinky curled  
  - Thumb checked to avoid misclassification  

- **Thumbs Up**  
  - Only thumb extended  
  - All other fingers curled  

---

