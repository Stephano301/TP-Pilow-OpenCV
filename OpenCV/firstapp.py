import numpy as np
import cv2 as cv

img = cv.imread('photo.png', cv.IMREAD_COLOR)
cv.imshow('image', img)
k = cv.waitKey(0) & 0xFF
if k == 27:             # attend la touche ESC pour quitter
    cv.destroyAllWindows()
elif k == ord('s'):     # attend la touche 's' pour sauvegarder et quitter
    cv.imwrite('messigray.png', img)
    cv.destroyAllWindows()