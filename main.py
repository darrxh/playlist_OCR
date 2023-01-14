from pytesseract import pytesseract
from tkinter import filedialog
from os import listdir
from os.path import isfile, join
import cv2
from matplotlib import pyplot

def load_tesseract():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    try:
        print (f"Running Tesseract Version: {pytesseract.get_tesseract_version()}")
    except Exception:
        print ("Tesseract Executable not found, please select from File Dialog")
        file_path_string = filedialog.askopenfilename()
        pytesseract.tesseract_cmd = file_path_string
        print (f"Running Tesseract Version: {pytesseract.get_tesseract_version()}")

def directory_prompt():
    print ("Select Directory with png screenshots...")
    path = filedialog.askdirectory(title='Select Folder')
    print (path)
    return path

def get_jpg_names(path):
    file_list = list()
    for file in listdir(path):
        full_path_name = join(path,file)
        if (isfile(full_path_name) and file.lower().endswith('.png')):
            file_list.append(full_path_name)
    print (file_list)
    return file_list

def opencv_filter(image_file):
    img = cv2.imread(image_file)
    #img = cv2.bitwise_not(img)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #img = cv2.medianBlur(img, 1)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return img


def print_string(full_name):
    print (pytesseract.image_to_string(full_name))

def main():
    load_tesseract()
    path = directory_prompt()
    file_list = get_jpg_names(path)
    processed_image = opencv_filter(file_list[0])
    print_string(processed_image)

if __name__ == '__main__':
    main()