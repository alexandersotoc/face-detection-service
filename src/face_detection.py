import cv2
from os import path, getcwd

cascPath = "./data/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

def find_faces(filename):
    file_path = path.join(getcwd(), 'uploads', filename)
    
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(200, 200),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    found_faces = []
    
    if (len(faces) > 0):
        found_faces = faces.tolist()

    result = {
        'number_faces': len(faces),
        'found_faces': found_faces
    }

    return result