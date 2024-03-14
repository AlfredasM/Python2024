import cv2
import matplotlib.pyplot as plt
import pandas as pd
import os


# #vaizdo ikelimas
# image = cv2.imread('paveikslelis.jpg')
#
# # parodyti orginalu vaizda
# cv2.imshow('Originalus vaizdas', image)
# cv2.waitKey(0)  # laukiama bet kokio klaviso paspaudimo
# cv2.destroyAllWindows()
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Pilku atspalviu vaizdas', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Modifikuokite veidų pavyzdį taip, kad galėtumėte eksperimentuoti su scaleFactor ir minNeighbors parametrais.
# Išbandykite skirtingas reikšmes ir stebėkite, kaip keičiasi veidų aptikimo rezultatai.


def find_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # ikeliame vaizda ir pakeisti i pilka
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # atrandame veidus vaizde
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.41, minNeighbors=5, minSize=(50, 50))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('veidai', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return faces


images_folder = 'C:/Users/Vartotojas/Desktop/veidai'
data = []

#files = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')]
#print(files)

for filename in os.listdir(images_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        path = os.path.join(images_folder, filename)
        faces = find_faces(path)
        data.append({'filename': filename, 'faces_count': len(faces)})

df = pd.DataFrame(data)

average_faces = df['faces_count'].mean()
#print(f'Vidutinis veidu skaicius vaizduose: {average_faces}')

# surasti vaizda su didziausiu veidu skaiciumi

max_faces = df.loc[df['faces_count'].idxmax()]
#print(f'Daugiausia veidu turintis vaizdas: {max_faces}, veidu skaicius: {max_faces["faces_count"]}')

df['faces_count'].plot(kind='hist', title="Veidu skaiciaus apsiskirstimas")
plt.xlabel("Veidu skaicius")
plt.ylabel("Vaizdu skaicius")
plt.show()

