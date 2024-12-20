import cv2
import mediapipe as mp
import pyautogui
import threading

pyautogui.FAILSAFE = False
class VideoCaptureThread:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src) # Inicializa la captura de video
        self.frame = None  # Inicializa la variable para almacenar el frame
        self.running = True # Indicador de si el hilo debe de seguir corriendo
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start() #Inicia el thread

    def update(self):
        while self.running:
            ret, frame = self.cap.read()#caputra un frame de la camara
            if ret:
                self.frame = cv2.flip(frame, 1) #Almacena el fram

    def read(self):
        return self.frame #devuelve el ultimo frame

    def stop(self):
        self.running = False
        self.thread.join()
        self.cap.release()#Finaliza la camara


cam = VideoCaptureThread(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Obtener la resolución actual de la pantalla
screen_w, screen_h = pyautogui.size()

# Factores para aumentar la sensibilidad en X e Y
x_sensitivity_factor = 2.5
y_sensitivity_factor = 3

# Bucle principal
try:
    while True:
        frame = cam.read()
        if frame is None:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks

        if landmark_points:
            landmarks = landmark_points[0].landmark

            forehead_landmark = landmarks[10]  # Punto de la frente
            chin_landmark = landmarks[152]  # Punto del mentón

            # Escalar las coordenadas del marco de la cámara a las coordenadas de la pantalla
            relative_x = (forehead_landmark.x - 0.5) * x_sensitivity_factor
            relative_y = ((forehead_landmark.y + chin_landmark.y) / 2 - 0.5) * y_sensitivity_factor

            # Calcular nueva posición del mouse basada en la posición de la cabeza
            new_mouse_x = int((relative_x + 0.5) * screen_w)
            new_mouse_y = int((relative_y + 0.5) * screen_h)

            # Limitar el movimiento del ratón dentro de la pantalla
            new_mouse_x = max(10, min(screen_w - 10, new_mouse_x))
            new_mouse_y = max(10, min(screen_h - 10, new_mouse_y))

            # Mover el ratón sin bloquear el proceso
            pyautogui.moveTo(new_mouse_x, new_mouse_y)

        # Mostrar la imagen de la cámara
        cv2.imshow("Head Controlled Mouse", frame)

        # Romper el bucle con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cam.stop()
    cv2.destroyAllWindows()
