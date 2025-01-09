import cv2
import numpy


#recortar, redimensionar y unir imagenes

# cargar la imagen fish
img = cv2.imread('resources/fish.png')

# imprimir en consola las dimensiones de la imagen
print(img.shape)

#redimensionar la imagen con otros valores
img_ancho = img.shape[1] #saco el ancho de la imagen
img_alto = img.shape[0] #saco el alto de la imagen

img_resized = cv2.resize(img, (300, 300)) #hacemos que la imagen mida 300x300, cuadrada


#redimensionar en relacion con el tamano de la imagen
img_resized_shape = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))#nos pide ancho y alto, que se encuentran en la pos 1 y 0

#recorte de parte de la imagen
#en el recorte hay que tener en cuenta el orden de los valores [y1:y2, x1:x2], como coordenadas en la imagen
image_crop = img[150:350, 300:500]

#hay que asegurarse de importar numpy al inicio para lo siguiente:
#combinar varias imagenes en horizontal (deben tener la misma altura y misma cantidad de canales de color, RGB)
image_horizontal = numpy.hstack((img_resized_shape, img_resized_shape))

#combinar varias imagenes en vertical (deben tener la misma anchura y misma cantidad de canales de color, RGB)
image_vertical = numpy.vstack((img_resized_shape, img_resized_shape))

cv2.imshow('original', img) #muestro la ventana original
cv2.imshow('img resized', img_resized) #muestro la imagen fish con el nuevo tamano
cv2.imshow('img resized shape', img_resized_shape) #muestro la imagen redimensionada en base a la original
cv2.imshow('iamge crop', image_crop)
cv2.imshow('image horizontal', image_horizontal)
cv2.imshow('image vertical', image_vertical)

cv2.waitKey(0) # salgo de la ejecucion de las ventanas


