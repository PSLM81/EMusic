#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import pygame
import random
import time

#creating and naming window
window = Tk()
window.title("First Window")
#Changing background colour
window.configure(background="black")
#Changing window size
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))

#Title
#Label (window,text="BGM SYSTEM", bg="black",fg="white", font="none 12 bold").grid(row=3, column=3, sticky=W+E)
pygame.mixer.init()


def tester():
    #Taking picture
    import cv2
    # initialize the camera
    cam = cv2.VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        # cv2.namedWindow("cam-test",cv2.CV_WINDOW_AUTOSIZE())
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cv2.waitKey(0)
        cv2.imwrite("emotion.jpg",img) #save image

        #Photo emotion recognition
    import tensorflow
    from fer import FER
    import matplotlib.pyplot as plt 
    get_ipython().run_line_magic('matplotlib', 'inline')

    test_image_one = plt.imread("emotion.jpg")
    emo_detector = FER(mtcnn=True)
    # Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(test_image_one)
    # Print all captured emotions with the image
    print(captured_emotions)
    plt.imshow(test_image_one)

    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    print(dominant_emotion, emotion_score)
    if (dominant_emotion == "angry"):
        pygame.mixer.music.load("angry_1.mp3")
    elif (dominant_emotion == "disgust"):
        pygame.mixer.music.load("disgust_1.mp3") 
    elif (dominant_emotion == "fear"):
        pygame.mixer.music.load("fear_1.mp3") 
    elif (dominant_emotion == "happy"):
        pygame.mixer.music.load("happy_1.mp3")
    elif (dominant_emotion == "sad"):
        pygame.mixer.music.load("sad_1.mp3") 
    elif (dominant_emotion == "surprise"):
        pygame.mixer.music.load("surprise_1.mp3")
    else:#neutral
        pygame.mixer.music.load("neutral_1.mp3")
    

soundplay = 0
music = "PAUSE"
def playsound():
    tester()
    global soundplay
    soundplay+=1
    if (soundplay==1):
        pygame.mixer.music.play()
        Button (window, image=pause, command=playsound, bd=0).place(relx=0.5, rely=0.5, anchor=CENTER)
    elif (soundplay%2==0):
        pygame.mixer.music.pause()
        Button (window, image=play, command=playsound, bd=0).place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        pygame.mixer.music.unpause()  
        Button (window, image=pause, command=playsound, bd=0).place(relx=0.5, rely=0.5, anchor=CENTER)

def close_window():
    window.destroy()
    pygame.mixer.music.stop()

        
#Use this for skipping - pygame.mixer.music.fadeout
back = PhotoImage(file="Back")
Button (window, image=back, bg="black", bd=0).place(relx=0.35, rely=0.5, anchor=CENTER)

play = PhotoImage(file="Play")
pause = PhotoImage(file="Pause")
Button (window, image=play, command=playsound, bd=0).place(relx=0.5, rely=0.5, anchor=CENTER)

next = PhotoImage(file="Next")
Button (window, image=next, bg="black", bd=0).place(relx=0.65, rely=0.5, anchor=CENTER)

exit = PhotoImage(file="exit1.gif")
Button (window, image=exit, command=close_window).place(relx=0.98, rely=0, anchor=N)

#running the main window
window.mainloop()

