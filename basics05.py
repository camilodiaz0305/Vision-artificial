import numpy
import cv2
import numpy as np

#funciones basicas de OpenCV para tratamiento de imagenes

#cargar la imagen
image = cv2.imread('resources/drawing.png')

#invertir los colores de nuestra imagen
#image_inverted = numpy.invert(image)
#o tambien con:
image_inverted = cv2.bitwise_not(image)

#cambio de espacio de color de BGR a HSV (matiz, saturacion y valor)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#DETECCION DE FORMAS, con un algoritmo que nos permite detectar bordes:

# 1. para reconocimiento de imagenes se usa la escala de grises, pasar imagen a grises
# 2. primero se aplica un algoritmo gaussiano para hacer un bloor y hacer que los bordes sean mas visibles
# 3. luego se aplica el algoritmo canny para detectar estos bordes, gauss le hace facil la vida a canny

#1. cambio de BGR a escala de grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#combinar, no puedo hacer esto porque al combinar deben ser ambas BGR o escala de grises:

# 2. Desenfoque gaussiano parametros (imagengris, matriz en donde se aplica el desenfoque, xsigma (variacion de desenfoque))
image_blur = cv2.GaussianBlur(image_gray, (11, 11), 0) #recordemos usar para esto la imagen en grises,
# en el kernel (segundo parametro), debe ser de tamano impar para que tenga centro, ademas debe ser cuadrado,
# por eso pusimos (11,11)
# enXsigma (tercer argumento) podemos poner cero para que calcule automaticamente esa variacion en x de desenfoque,
# no es necesario hacerlo en Y

# 3. detector de bordes canny: parametro (pasar la desenfocada, (limites en donde epieza a detectar el borde (inferior, superior)))
image_canny = cv2.Canny(image_blur, 50, 100)

#hay un problema, al hacer esto por ejemplo en el cuadrado detecta 2 bordes, por su grosor,
# cuando canny lo senale van a aparecer a simple vista 2 cuadrados por su borde interno y externo,
# si vamos a detectar el cuadrado en especifico va a detectar 2 cuadrados y eso no es verdad

#que hacemos: dilatacion y erosionar ... requerimos un kernel de unos:
kernel = numpy.ones((5, 5), np.uint8)
#la dilatacion hace que los pixeles cercanos a los blancos sean mas blancos, osea que las lineas blancas van a ser gruesas
image_dilation = cv2.dilate(image_canny, kernel, iterations=2) # cuantas mas iteraciones, mas dilatacion

#erosion de las lineas dilatadas previamente:
image_eroded = cv2.erode(image_dilation, kernel, iterations=1)

#obtencion de una imagen binaria mediante umbrales, convertirla en puro blanco y negro:
#devuelve dos valores, asi que se almacena en 2 variables: #debe ser una imagen que haya sido puesta en escala de grises y se le haya hecho un gauss
# igual que lo que pide el canny, asi que le pasamos la imagen blur, que tiene el desenfoque gaussiano
ret, image_thresh = cv2.threshold(image_blur, 100, 255, cv2.THRESH_BINARY_INV)

# el 100, los valores por dabajo vana  ser negros, y por encima de 100 va a ser blanco
# el 255 es por que debe ser el maximo
#inv, invierto los colores blanco y negro si quiero

#debo cambiar espacio de color para combinar las imagenes:
image_gray = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
image_blur = cv2.cvtColor(image_blur, cv2.COLOR_GRAY2BGR)
image_canny = cv2.cvtColor(image_canny, cv2.COLOR_GRAY2BGR)
image_dilation = cv2.cvtColor(image_dilation, cv2.COLOR_GRAY2BGR)
image_eroded = cv2.cvtColor(image_eroded, cv2.COLOR_GRAY2BGR)
image_thresh = cv2.cvtColor(image_thresh, cv2.COLOR_GRAY2BGR)

#Ahora si, combino imagenes en horizontal:
image_canny_horizontal = numpy.hstack((image, image_gray, image_blur, image_canny, image_dilation, image_eroded))
image_thresh_horizontal = numpy.hstack((image, image_gray, image_blur, image_thresh))

#mostrar la imagen
cv2.imshow('image', image_canny_horizontal)
cv2.imshow('image_thresh', image_thresh_horizontal)
#cv2.imshow('image_inverted', image_inverted)
#cv2.imshow('image espacio de color', image_hsv)
#esperar
cv2.waitKey(0)