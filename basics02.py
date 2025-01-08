import cv2

# descargar un video de disco y reproducirlo

# cargar el video de disco
capture = cv2.VideoCapture("resources/video.mp4")

# si quiero mostrar la imagen de mi camara, el indice es cero:
#capture = cv2.VideoCapture(0)
#pero si mi camara funciona a 60 fps, cambio el valor del stop abajo, el que cierra el bucle

#recorrer cada frame del video con un bucle
while True:
    ret, frame = capture.read() # read() devuelve dos cosas, por eso se guarda en dos variables ret y frame
    # en ret, se guarda un booleano, verdadero si el frame es valido, falso si no.
    # frame es la imagen como tal

    if ret: ## si el ret es true, continue leyendo frames y muestre el actual con la siguiente funcion
        #mostrar el frame del video
        cv2.imshow("Frame", frame);

    #hacemos la espera en la muestra del frame cada 1 ms, si pulsamos 'q' cerramos ese frame forzosamente y el while
    #porque le pusimos un brake
    #if cv2.waitKey(1) & 0xFF == ord('q'): break ##salimos del bucle con break

    #colocar los segundos para que se ejecute a velocidad normal
    # dividimos 1 seg (1000 ms) entre los frames reales del video que son 25 frames por segundo, eso lo veo en detalles del video
    if cv2.waitKey(1000//25) & 0xFF == ord('q'):
        break

    #el break de la camara:
    #if cv2.waitKey(1000 // 60) & 0xFF == ord('q'):
    #    break