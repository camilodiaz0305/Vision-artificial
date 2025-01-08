import cv2
import numpy as np


#recortar, redimensionar y unir imagenes

# cargar la imagen fish
img = cv2.imread('resources/fish.png')

print(img.shape)

#redimensionar la imagen con otros valores
img_ancho = img.shape[1] #saco el ancho de la imagen
img_alto = img.shape[0] #saco el alto de la imagen

img_resized = cv2.resize(img, (300, 300)) #hacemos que la imagen mida 300x300, cuadrada

cv2.imshow('original', img) #muestro la ventana original
cv2.imshow('img resized', img_resized) #muestro la imagen fish con el nuevo tamano

cv2.waitKey(0) # salgo de la ejecucion de las ventanas

# imprimir en consola las dimensiones de la imagen
