from statistics import mode
import os
import cv2
from keras.models import load_model
import numpy as np
import sys



from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input


def detection_FER(image):
    try:



        # parameters for loading data and images
        detection_model_path = '../FER_CNN/models/haarcascade_frontalface_default.xml'
        emotion_model_path = '../FER_CNN/models/cnn_model.hdf5'
        emotion_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy',4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

        # hyper-parameters for bounding boxes shape
        frame_window = 10
        emotion_offsets = (20, 40)
        emotion_text = ""

        # loading models
        face_detection = load_detection_model(detection_model_path)
        emotion_classifier = load_model(emotion_model_path, compile=False)

        # getting input model shapes for inference
        emotion_target_size = emotion_classifier.input_shape[1:3]

        # starting lists for calculating modes
        emotion_window = []

        # starting video streaming
        bgr_image = cv2.imread(image)
        #print(bgr_image)
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces = detect_faces(face_detection, gray_image)
        #print(faces)
        for face_coordinates in faces:
            print(face_coordinates)

            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue

            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            print(emotion_text)
            emotion_window.append(emotion_text)


            if len(emotion_window) > frame_window:
                emotion_window.pop(0)
            try:
                emotion_mode = mode(emotion_window)
            except:
                continue

            if emotion_text == 'Angry':
                color = emotion_probability * np.asarray((255, 0, 0))
            elif emotion_text == 'Sad':
                color = emotion_probability * np.asarray((0, 0, 255))
            elif emotion_text == 'Happy':
                color = emotion_probability * np.asarray((255, 255, 0))
            elif emotion_text == 'Surprise':
                color = emotion_probability * np.asarray((0, 255, 255))
            elif emotion_text=='Neutral':
                color = emotion_probability * np.asarray((0, 255, 255))
            elif emotion_text=='Fear':
                color = emotion_probability * np.asarray((0, 255, 255))
            else:
                color = emotion_probability * np.asarray((0, 255, 0))

            color = color.astype(int)
            color = color.tolist()

            draw_bounding_box(face_coordinates, rgb_image, color)
            draw_text(face_coordinates, rgb_image, emotion_mode,color, 0, 0, 2, 2)



            bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite("result.jpg",bgr_image)

            #cv2.imshow('Face Expression Recognition', bgr_image)

            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        return emotion_text
    except Exception as e:
        print("Error=" + e.args[1])
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)


#if __name__=="__main__":
 #   detection_FER('../FER_CNN/testimages/sad.jpeg')
