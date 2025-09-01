import cv2
import numpy as np

# Cargar modelo DNN de Caffe
net = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt',
    'res10_300x300_ssd_iter_140000.caffemodel'
)

# Inicializar la cámara
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    (h, w) = frame.shape[:2]

    # Crear blob
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # Pasar por la red
    net.setInput(blob)
    detections = net.forward()

    # Dibujar rectángulos en rostros detectados
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, f"{confidence*100:.1f}%", (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame
    cv2.imshow("Detección de rostros", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()