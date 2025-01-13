from operator import length_hint

import cv2

#Ejercicio de deteccion de figuras geometricas

#obtener funcionn formas de la figura

def get_shapes(input_image_canny, input_image_contour):
    #obtenemos los contornos
    contours, hierarchy = cv2.findContours(input_image_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #hierarchy nos define si la figura es normal o está dentro de otra figura
    #RETR EXTERNAL define recupera los contornos exteriores solamente, si hay una figura dentro, no la recupera

    #contador para contar figuras del mismo tipo:
    triangle_count = 0
    square_count = 0
    rectangle_count = 0
    pentagon_count = 0
    hexagon_count = 0
    circle_count = 0

    #recorremos cada contorno de la iamgen con un bucle:
    for contour in contours:
        #dibujamos todos los contornos encontrados:
        #parametros de drawcontorns (imagen, contorno, ID o -1 para dibujar todos, color, grosor)
        #cv2.drawContours(input_image_contour, contour, -1, (255, 0, 0), 2)

        #obtenemos el area
        area = cv2.contourArea(contour)
        print("Area: " + str(area))

        #se obtiene la longitud del contorno
        perimeter = cv2.arcLength(contour, True) # el segundo parametro es por si el contorno es abierto o cerrado, si es cerrado es true
        print("Perimeter: " + str(perimeter))

        #se aproxima la curva poligonal, con error de 1% (contorno, error en base al perimetro, )
        poly = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

        # si pasamos el parametro directamente, la funcion dibuja los puntos de la curva
        cv2.drawContours(input_image_contour, poly, -1, (255, 0, 0), 2)

        #si pasamos el poly entre corchetes se interpreta como una lista y se dibuja el poligono
        cv2.drawContours(input_image_contour, [poly], -1, (255, 0, 0), 2)

        #se obtiene la longitud del contorno (x y es posicion, w ancho, h alto):
        x, y, w, h = cv2.boundingRect(poly)

        #dibujamos el rectangulo
        cv2.rectangle(input_image_contour, (x, y), (x + w, y + h), (0, 255, 0), 2, cv2.FILLED)

        #calculamos el centro del rectangulo:
        center = (x + w // 2, y + h // 2)
        #dibujamos un punto en el centro del rectangulo
        cv2.circle(input_image_contour, center, 1, (0, 255, 0), 2, cv2.FILLED)
        print("position "+str(center))

        #cuantos vertices tiene la figura:
        corner_count = len(poly)
        print("corner_count: " + str(corner_count))

        #ponemos el nombre de la figura
        if corner_count == 3:
            obj_type = "triangle"
            triangle_count += 1
        elif corner_count == 4:
            #puede ser cuadrado o rectangulo, miramos relacion entre altura y ancho
            aspect_ratio = w / h
            if (aspect_ratio) > 0.95 and (aspect_ratio < 1.05):
                obj_type = "square"
                square_count += 1
            else:
                obj_type = "rectangle"
                rectangle_count += 1
        elif corner_count == 5:
            obj_type = "pentagon"
            pentagon_count += 1
        elif corner_count == 6:
            obj_type = "hexagon"
            hexagon_count += 1
        else:
            obj_type = "circle"
            circle_count += 1
        #anotamos la imagen con el tipo de figura:
        cv2.putText(input_image_contour, obj_type, center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        #imprimimos los datos encontrados
        print(obj_type + " with area " + str(area) + " at "+ str(center))

    #imprimimos el numero de figura de cada tipo:
    print("triangle_count: " + str(triangle_count))
    print("square_count: " + str(square_count))
    print("rectangle_count: " + str(rectangle_count))
    print("pentagon_count: " + str(pentagon_count))
    print("hexagon_count: " + str(hexagon_count))
    print("circle_count: " + str(circle_count))

#cargamos la imagen

image = cv2.imread('resources/shapes.png')


image_contour = image.copy()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_blur = cv2.GaussianBlur(image_gray, (3, 3), 0)

image_canny = cv2.Canny(image_blur, 50, 100)

get_shapes(image_canny, image_contour)

#guardaremos la imagen resultante en  la carpeta resources:
cv2.imwrite('resources/result.png', image_contour)

#vemos el resultado
cv2.imshow('image', image_contour)
cv2.waitKey(0)