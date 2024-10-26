<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# SHIBUDINAM APP 🎯


## Basic Details
### Team Name:Hakuna Matata


### Team Members
- Team Lead: Hridhika Satheesh - TKMCE
- Member 2: Ann Maria jose-TKMCE
- Member 3: Sneha SK - TKMCE

### Project Description
The project is a motivational app that detects the users emotions and generates motivation memes .
Sometimes, the memes could be offensive in a way to make the situation funny. 


### The Problem (that doesn't exist)
Th problem could be lack of motivation 

### The Solution (that nobody asked for)
[How are you solving it? Keep it fun!]
We are giving an application to make the situation funny and intersting.


## Technical Details
### Technologies/Components Used
For Software:
- Flask,Python
- HTML
- CSS
- Javascript




### Implementation
For Software:
# Installation
pip install flask
pip install tensorflow
pip install opencv-python
pip install flask-cors fer


# Run
# Start the Flask server
python app.py


### Project Documentation
For Software:


Overview
SHIBUDINAM is a Flask-based web application that detects users' emotions via a webcam feed and serves personalized meme videos corresponding to the detected expression. The project uses machine learning with TensorFlow for emotion analysis, OpenCV for video capture and image processing, and a frontend interface that presents an interactive and aesthetic user experience.

Project Architecture
Frontend:

HTML, CSS, and JavaScript are used to build a responsive user interface with an embedded webcam view.
A button allows the user to capture an image, which is sent to the backend for emotion analysis.
The application displays a corresponding meme video based on the detected emotion.
Backend:

Flask serves as the backend framework, managing routes and processing requests.
TensorFlow and FER (Facial Expression Recognition) are employed to analyze captured images and determine emotions.
Based on the emotion detected, Flask retrieves an appropriate meme video stored locally.
Data Flow:

The frontend sends the captured image to the backend.
The backend uses TensorFlow and FER for emotion detection.
Based on the emotion, a random meme video is selected from the predefined library and served back to the user.




# Screenshots (Add at least 3)
![image](https://github.com/user-attachments/assets/08b37d3d-9af6-4fe2-9bf7-a10ef5e610b9)
This is when the user looks happy.


![image](https://github.com/user-attachments/assets/485b9416-764b-42c2-94db-11c4079054af)
![Screenshot2](Add screenshot 2 here with proper name)


*Add caption explaining what this shows*

![image](https://github.com/user-attachments/assets/ed7195eb-b587-4f8c-9af1-262dc6896ac2)
This is when the user looks neutral


# Diagrams
+-------------------------+                  +--------------------+
|                         |                  |                    |
|  Client (Web Interface) |                  |   Flask Server     |
|                         |                  |                    |
+-------------------------+                  +--------------------+
          |                                         |
          | 1. Capture User Image via Webcam        |
          +---------------------------------------> |
          |                                         |
          |                                         |
          |                                         | 2. Process Image (OpenCV & FER)
          |                                         |
          |                                         |
          |                                         v
          |                                +--------------------+
          |                                |                    |
          |                                |  Emotion Detection |
          |                                |                    |
          |                                +--------------------+
          |                                         |
          |                                         |
          |                                         | 3. Determine Detected Emotion
          |                                         | and Select Video URL
          |                                         |
          |                                         v
          |                               +---------------------+
          |                               |                     |
          |                               | Video Selector (by  |
          |                               | Emotion Category)   |
          |                               +---------------------+
          |                                         |
          |                                         |
          |                                         | 4. Return Video URL and Message
          |                                         |
          +-----------------------------------------+
          |                                         |
          |                                         v
+-------------------------+                 +----------------------+
|                         |                 |                      |
|    Display Video for    |                 |     Local Storage    |
|    Detected Emotion     |                 |    (Static Videos)   |
|                         |                 |                      |
+-------------------------+                 +----------------------+





### Project Demo
# Video
[[Add your demo video link here]](https://drive.google.com/file/d/130wHhlq8LfOG8BDsBgLcBiPdFwAnIumU/view?usp=sharing)
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

Ann Maria: Led the development of the Flask server, implemented the emotion detection feature with FER and OpenCV, and handled video selection logic based on detected emotions.
Hridhika: Designed and built the front-end interface using HTML, CSS, and JavaScript, implemented webcam integration, and styled the page for an engaging user experience.
Managed project documentation, created the workflow and architecture diagrams, and coordinated the integration of components, testing the end-to-end user flow and debugging across the stack.
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



