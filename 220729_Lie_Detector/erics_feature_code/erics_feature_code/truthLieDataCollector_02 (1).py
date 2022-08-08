# https://google.github.io/mediapipe/solutions/face_mesh.html#:~:text=MediaPipe%20Face%20Mesh%20is%20a,for%20a%20dedicated%20depth%20sensor.

## DEPENDANCIES ##
# pip3 install opencv-python
# pip3 install cv2
# pip3 install mediapipe
# pip3 install keyboard
# winsound may not work on Mac OS - replace with Mac system sounds

import cv2
import mediapipe as mp
import itertools
import keyboard
import winsound
import re, os

#  This program will open up a webcam window and draw any facial features
# it finds on a face if it finds one. It will output two sets of x,y,z
# positional coordinates per eye per frame. If you press "T" for a "true" data instance
# (or any other acceptable truth keypress - see implementation), for example, it will
# begin to record the data and the video, and if you press "T" again, it will
# stop recording data and video. If you then, press "S", it will save it to a
# folderName folder as two files - the video in its own named by the first 20
# characters of the data, and the data itself will be appended to a fileName
# file. Note, the data can be matched to the video filename easily by the fileName.
# If you similarly press "F", the same process produces a "lie" tagged data set, and
# if you press "D", the data and video will be deleted (in the case of an error
# in recording.
# Pressing "Z" ends the program.
# Note: this implementation is not particularly fault tolerant of mixing up the
# keypresses, so be careful. A sound accompanies the funtions to help make sure
# you are doing what you think you are doing. If you do not hear the appropriate sound,
# you may need to press the key again... it has sluggish response time.
#

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# file name of the data file -- adjust for path
folderName = "vids"
fileName = folderName + "/" + "truthLieData.txt"

if not os.path.exists(folderName):
    os.mkdir(folderName)


def saveData(dataInput, file=fileName):
    with open(file, "a") as f:
        for each in dataInput:
            f.write(each)
        f.write("================================================================\n")
    print("data saved **************************")


# customizable keys to trigger events
truthKeys = ["a", "t"]  # start/stop recording truth
lieKeys = ["l", "f"]  # start/stop recording lie
saveKeys = ["x", "s"]  # save recording to fileName
deleteKeys = ["m", "d"]  # delete recording (from memory only)
endProgKeys = ["z", "e"]  # end program (might need to hold it down)

frameCount = 0

isRecording = False  # flags when recording starts
wasRecording = False  # flags when first recorded frame happens
vidOut = ""  # name of video output file

endProg = False
isLie = 0  # set to 1 for true
# data format:  [t/f, frame, [xL yL zL xL yL zL xR yR zR xR yR zR]]
#               [t/f, frame, [xL yL zL xL yL zL xR yR zR xR yR zR]]
#               [t/f, frame, [xL yL zL xL yL zL xR yR zR xR yR zR]]
#               [t/f, frame, [xL yL zL xL yL zL xR yR zR xR yR zR]]
#               ===================================================

# raw video capture filename format:
#           data from first line of captured data during the video
#           For example, if first line of captured data is:
#                   [0, 5, [x:0.6005527377128601y:0.5324121713638306z:0.01530668884515...
#           The fileName will be "0_5_x0.6005527377128.avi"

data = []

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")


with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as face_mesh:
    while cap.isOpened():
        # play a sound and start or stop recording
        for each in lieKeys:
            if keyboard.is_pressed(each):
                if isRecording:
                    print(
                        "stop recording lie ********************************************************"
                    )
                    isRecording = False
                    wasRecording = False
                    winsound.Beep(240, 500)
                else:
                    print(
                        "start recording lie ********************************************************"
                    )
                    isRecording = True
                    wasRecording = False
                    isLie = 0
                    data = []
                    winsound.Beep(440, 500)

        for every in truthKeys:
            if keyboard.is_pressed(every):
                if isRecording:
                    print(
                        "stop recording truth ********************************************************"
                    )
                    isRecording = False
                    wasRecording = False
                    winsound.Beep(1240, 500)
                else:
                    print(
                        "start recording truth ********************************************************"
                    )
                    isRecording = True
                    wasRecording = False
                    isLie = 1
                    data = []
                    winsound.Beep(1440, 500)

        # press save keys to save data to disk and clear data
        for one in saveKeys:
            if keyboard.is_pressed(one):
                if isRecording == False:
                    # output video file #########################################
                    print(f"saving video {vidOut}*************")
                    out.release()
                    wasRecording = False

                    if len(data) > 0:
                        saveData(data)
                        winsound.Beep(800, 250)
                        winsound.Beep(800, 250)
                        data = []

        # press delete keys to delete recording and clear data
        for other in deleteKeys:
            if keyboard.is_pressed(other):
                winsound.Beep(140, 250)
                winsound.Beep(140, 250)
                isRecording = False
                wasRecording = False
                print(f"deleting video {vidOut}***************")
                if os.path.exists(vidOut):
                    out.release()
                    os.remove(vidOut)

                ###################################3out.destroyVideo()
                data = []

        for these in endProgKeys:
            if keyboard.is_pressed(these):
                endProg = True
                print("End Program *********************")

        if endProg == True:

            cap.release()
            out.release()
            break

        success, image = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        LEFT_EYE_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_LEFT_EYE)))
        RIGHT_EYE_INDEXES = list(set(itertools.chain(*mp_face_mesh.FACEMESH_RIGHT_EYE)))

        # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                frameCount = frameCount + 1
                print("frame: ", frameCount)
                print(f"LEFT EYE LANDMARKS:n")

                tempData = []
                for LEFT_EYE_INDEX in LEFT_EYE_INDEXES[:2]:

                    print(face_landmarks.landmark[LEFT_EYE_INDEX])
                    tempData.append(face_landmarks.landmark[LEFT_EYE_INDEX])

                print(f"RIGHT EYE LANDMARKS:n")

                for RIGHT_EYE_INDEX in RIGHT_EYE_INDEXES[:2]:

                    print(face_landmarks.landmark[RIGHT_EYE_INDEX])
                    tempData.append(face_landmarks.landmark[RIGHT_EYE_INDEX])

                ################## RECORD DATA and VIDEO

                if isRecording == True:  # start recording data
                    stringToAppend = f"[{isLie}, {frameCount}, ["
                    for each in tempData:
                        stringToAppend = stringToAppend + re.sub("\s+", "", str(each))
                    stringToAppend = stringToAppend + "]]\n"
                    data.append(stringToAppend)

                    if wasRecording == False:  # start recording video
                        # start recording video
                        wasRecording = True  # only do this on first frame

                        firstChars = str(stringToAppend)[:20]
                        firstChars = re.sub("\s+", "", str(firstChars).replace(":", ""))
                        firstChars = firstChars.replace("[", "")
                        firstChars = firstChars.replace(",", "_")

                        vidOut = f"{folderName}/{firstChars}.avi"
                        out = cv2.VideoWriter(vidOut, fourcc, 20.0, (640, 480))

                    if wasRecording == True:
                        print(
                            f"outputing frame {vidOut} *************************"
                        )  #############
                        out.write(image)

                tempData = []

                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style(),
                )
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow("MediaPipe Face Mesh", cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
