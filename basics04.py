import numpy
import cv2

#dibujar formas geometricas, guardar en el disco, etc, esto sirve para la actividad, debo guardar las imagenes para ponerlas en el pdf

#modificar cada valor de la matriz de la imagen, RGB son 3 valores distintos, modificar los 3 valores por cada pixel

#primero hacemos una imagen vacia, una matriz de ceros, el cero representa el negro, imagen cuadrada de 400x400 px:
#ojo, python usa BGR, al reves de RGB

image = numpy.zeros((400, 400, 3), numpy.uint8) #numpy nos ayuda a crear la matriz, la funcion zeros nos hace una matriz de ceros

#se puede acceder a los valores de la matriz  para aplicar un valor
# para modificar TODOS los pixeles ponemos como indice '[:]'

image[:] = (255, 0, 0) #BGR

#del mismo modo si queremos aplicar un tono de gris, se puede usar la misma sintaxis

image[::] = 120

#poner el color solamente en una zona y no en toda la imagen, primer rango de valores en y y el otro en x, como coordenadas
#image[y1:y2, x1:x2]

image[20:380, 20:380] = (50,60,100) #20 y 380 significa que dejo un margen de 20 px en x & en y en forma de cuadrado

#las funciones de dibujo modifican la imagen que se les pase: (todas piden como parametro inicial la imagen a modificar)

#linea: parametros(imagen, punto de origen, punto final, color, grosor de la linea) cv2

cv2.line(image, (150, 150), (250, 50), color = (50, 50, 255), thickness = 3)

#rectangulo: parametros(imagen, esquina inicial, esquina final, color, grosor, tipo de linea)

cv2.rectangle(image, (150, 150), (250, 250), color = (60, 150, 255), thickness = 3)

#circulo: centro, radio, color, grosor, (si es -1 se rellena), tipo de linea
cv2.circle(image, (150, 150), 50, color = (60, 150, 255), thickness = 3)

#texto: parametros(texto, origen, fuente, tamano, color, grosor)
cv2.putText(image, "openCV", (80, 340), cv2.FONT_HERSHEY_SIMPLEX, fontScale = 2, color = (255, 255, 255))

#guardar la imagen resultante en disco, la guardaremos en "resources": parametros(ruta con el nombre de la imagen y formato, imagen)
cv2.imwrite("resources/drawing.png", image)

#mostrar la imagen
cv2.imshow("image", image)


cv2.waitKey(0)





