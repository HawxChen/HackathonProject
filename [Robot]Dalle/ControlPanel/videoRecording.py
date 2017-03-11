import numpy as np
import cv2
import os

def videoRecording():
    turn = False;
    framerate = 20.0

    cap = cv2.VideoCapture(0)
    videoLength = 10
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    while True:
        if not turn: 
            out = cv2.VideoWriter('./myvideo1.avi', fourcc, framerate, (640, 480))
            turn = True
        else:
            out = cv2.VideoWriter('./myvideo2.avi', fourcc, framerate, (640, 480))
            turn = False
        for i in xrange(videoLength*framerate()):
            ret, frame = cap.read()
            out.write(frame)
        out.release()
    cap.release()

videoRecording()

