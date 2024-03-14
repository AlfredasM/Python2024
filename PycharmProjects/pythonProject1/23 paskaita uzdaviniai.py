# * Vaizdo Įkėlimas ir Rodymas
#         Parašykite programą, kuri įkelia ir parodo vaizdą naudojant OpenCV. Eksperimentuokite su įvairiais vaizdais.
#     * Vaizdo Konvertavimas į Pilkus Atspalvius
#         Modifikavus pirmąją programą, pridėkite funkcionalumą vaizdo konvertavimui į pilkus atspalvius prieš jį rodant.
#     * Vaizdo Išsaugojimas
#         Įkelkite vaizdą, pakeiskite jį į pilkus atspalvius.

import cv2
import os
image_path = r'C:\Users\Vartotojas\Desktop\vaizdas2\tree.jpg'
directory = r'C:\Users\Vartotojas\Desktop\vaizdas2'

img = cv2.imread(image_path)

cv2.imshow('Originalus vaizdas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Pilkas vaizdas', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

pilkafoto = 'pilkafoto.jpg'
os.chdir(directory)

img_saved = cv2.imwrite(pilkafoto, gray_image)

print(os.listdir(directory))