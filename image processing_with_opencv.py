from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse
import time
from imutils.object_detection import non_max_suppression
import os

# net = cv2.dnn.readNet(model)

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-i", "--image", type=str,
                            help="path to input image")
argumentParser.add_argument("-east", "--east", type=str,
                            help="path to input EAST Detector")
argumentParser.add_argument("-c", "--min-confidence", type=float,
                            default=0.5, help="minimum probability required to inspect a region")
argumentParser.add_argument("-w", "--width", type=int,
                            default=32, help="resized image width(should be multiple of 32)")
argumentParser.add_argument("-e", "--height", type=int,
                            default=32, help="resized image height(should be multiple of 32)")
args = vars(argumentParser.parse_args())


def get_string():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = cv2.imread('image_grubhub.jpg', cv2.COLOR_BGR2RGB)
    # image = cv2.resize(image, (1350, 750))
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)
    plt.imshow(image)
    plt.show()
    pass


print('--Recognize text--')
print(get_string())


# cv2.imshow('image', image)
# cv2.waitKey()
cv2.destroyAllWindows()
