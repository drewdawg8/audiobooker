from PIL import Image
import pytesseract
import argparse
import cv2
import os
import codecs

def parse_text(img):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename,gray)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    textfile = codecs.open("text.txt", "w+", encoding="utf-8")
    textfile.write(text)
    textfile.close()
    return text
