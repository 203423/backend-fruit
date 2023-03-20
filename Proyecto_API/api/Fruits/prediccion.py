import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2


def load_img(filename):
    rootdir = 'assets'
    for subdir , dirs , files in os.walk(rootdir):
        for file in files:

            frame = cv2.imread(os.path.join(subdir, file))


            if frame is None:
                print("not an image")
            else:
                print(subdir,file)
                resizedBig = resized = cv2.resize(frame,(280,280), interpolation=cv2.INTER_AREA)
                resized = cv2.resize(frame,(28,28), interpolation=cv2.INTER_AREA)
                
    return resized



def HacerPrediccion(sonido_predecir):
    frutas = ["apple","cucumber","greentomato","Guineo","lemon","lemontangerine","mango","potato","Uva"]
    # sonido_predecir = os.path.join('assets/pruebaViolin.wav')
    img = load_img(sonido_predecir)

    img=np.expand_dims(img, axis=0)
    modeloCNN = tf.keras.models.load_model('api/Fruits/fruit_model.h5')
    prediction = modeloCNN.predict(img)
    predicted_label = np.argmax(prediction, axis=1)
    instrumento = frutas[predicted_label[0]]
    print("La fruta es: ", instrumento)
    return instrumento
    
