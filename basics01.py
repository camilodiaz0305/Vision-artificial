import cv2
import numpy as np

# Cargar una imagen de disco y mostrarla

# cargar la imagen fish
img = cv2.imread('resources/fish.png')
cv2.imshow('fish', img) #muestro la imagen fish, el primer parametro es el nombre de la ventana de la imagen
#cv2.waitKey(0) # espera a que se active una senal para que continue el programa, en este caso una interaccion

# cargar la imagen shapes
img2 = cv2.imread('resources/shapes.png')
cv2.imshow('shapes', img2) #muestro la imagen shapes, el primer parametro es el nombre de la ventana de la imagen
cv2.waitKey(0) # espera a que se active una senal para que continue el programa, en este caso una interaccion

cv2.destroyAllWindows()


