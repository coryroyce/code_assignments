""" 
Import Local Video and with OpenCV and save it after processing
Update 8/7/2022

Note:
- Need to `pip install opencv-python`
- Need to `pip install opencv-contrib-python`

"""

import cv2
import numpy as np
import os
import time
import mediapipe as mp

video_path = "reference/Cory_T_01.mp4"
# cap = cv2.VideoCapture(video_path)

mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities


def main():
    """Run the main video conversion function"""
    # Set mediapipe model
    with mp_holistic.Holistic(
        min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as holistic:
        cap = cv2.VideoCapture(video_path)

        if cap.isOpened():
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            res = (int(width), int(height))
            # this format fail to play in Chrome/Win10/Colab
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # codec
            # fourcc = cv2.VideoWriter_fourcc(*"H264")  # codec
            out = cv2.VideoWriter("output.mp4", fourcc, 20.0, res)

            frame = None
            while True:
                try:
                    is_success, frame = cap.read()
                except cv2.error:
                    continue

                if not is_success:
                    break

                # OPTIONAL: do some processing
                # Make detections
                image, results = mediapipe_detection(frame, holistic)

                # Draw landmarks
                draw_styled_landmarks(image, results)

                # # convert cv2 BGR format to RGB
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # out.write(frame)
                out.write(image)

            out.release()

        cap.release()

    return


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # Image is no longer writeable
    results = model.process(image)  # Make prediction
    image.flags.writeable = True  # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR COVERSION RGB 2 BGR
    return image, results


def draw_landmarks(image, results):
    # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS) # Draw face connections
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS
    )  # Draw pose connections
    mp_drawing.draw_landmarks(
        image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS
    )  # Draw left hand connections
    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS
    )  # Draw right hand connections


def draw_styled_landmarks(image, results):
    # # Draw face connections
    # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
    #                          mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
    #                          mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
    #                          )
    # Draw pose connections
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
        mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2),
    )
    # Draw left hand connections
    mp_drawing.draw_landmarks(
        image,
        results.left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
        mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2),
    )
    # Draw right hand connections
    mp_drawing.draw_landmarks(
        image,
        results.right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
    )


if __name__ == "__main__":
    main()


"""A Working version to save a local file"""

# import cv2

# video_path = "reference/Cory_T_01.mp4"
# cap = cv2.VideoCapture(video_path)


# if cap.isOpened():
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     res = (int(width), int(height))
#     # this format fail to play in Chrome/Win10/Colab
#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # codec
#     # fourcc = cv2.VideoWriter_fourcc(*"H264")  # codec
#     out = cv2.VideoWriter("output.mp4", fourcc, 20.0, res)

#     frame = None
#     while True:
#         try:
#             is_success, frame = cap.read()
#         except cv2.error:
#             continue

#         if not is_success:
#             break

#         # OPTIONAL: do some processing

#         # convert cv2 BGR format to RGB
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

#         out.write(frame)

#     out.release()

#     # OPTIONAL: show last image
#     if frame:
#         cv2_imshow(frame)

# cap.release()


# import numpy as np
# import cv2 as cv

# local_video_path = "/reference/Cory_T_01.mp4"
# cap = cv.VideoCapture(local_video_path)
# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*"XVID")
# # fourcc = cv.VideoWriter_fourcc(*"DIVX")

# out = cv.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
#     # write the flipped frame
#     out.write(frame)
#     cv.imshow("frame", frame)
#     if cv.waitKey(1) == ord("q"):
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()
