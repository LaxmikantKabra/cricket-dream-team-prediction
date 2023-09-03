import os
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pdf2image.pdf2image as p2i
from PIL import Image
from matplotlib.widgets import RectangleSelector
import pytesseract as pt

# '''
# this is a properly working code chunk to extract coordinates
# Using plt.imread() to reads the image file and return a NumPy array of the image data.
image = plt.imread("./4002_old/4002_response1_pg2.jpg")

# Import the rectangle selector
# This widget allows the user to select a rectangular region on the image by clicking and dragging the mouse.

# function called when the user selects a region
# It takes two arguments eclick and erelease, which represent the mouse click event and the mouse release event respectively.
# Setting four global variables x1, y1, x2, and y2 to the coordinates of the top-left and bottom-right corners of the selected rectangle


def onselect(eclick, erelease):
    global x1, y1, x2, y2
    x1, y1 = int(eclick.xdata), int(eclick.ydata)
    x2, y2 = int(erelease.xdata), int(erelease.ydata)
    print(f"({x1}, {y1}), ({x2}, {y2})")


# creates a new figure and returns a tuple containing the figure object and a single axis object. ax.imshow() displays the image on the axis.
fig, ax = plt.subplots()
ax.imshow(image)

# Create the rectangle selector
rs = RectangleSelector(ax, onselect)
plt.show()

# end_of_function
# '''

# Define the coordinates of the sub-images
# coordinates with questions not included
page_dist_coords = {'q1': {'x1': 0, 'y1': 345, 'x2': 855, 'y2': 1060},
                    'q2': {'x1': 855, 'y1': 335, 'x2': 1690, 'y2': 1060},
                    'q3': {'x1': 0, 'y1': 1175, 'x2': 855, 'y2': 2195},
                    'q4': {'x1': 855, 'y1': 1105, 'x2': 1699, 'y2': 2195},
                    'q5': {'x1': 0, 'y1': 330, 'x2': 855, 'y2': 1020},
                    'q6': {'x1': 855, 'y1': 310, 'x2': 1685, 'y2': 1020},
                    'q7': {'x1': 0, 'y1': 1035, 'x2': 855, 'y2': 1915},
                    'q8': {'x1': 855, 'y1': 1125, 'x2': 1695, 'y2': 1910},
                    'box': {'x1': 615, 'y1': 1995, 'x2': 730, 'y2': 2050},
                    'dg1': {'x1': 605, 'y1': 1990, 'x2': 665, 'y2': 2050},
                    'dg2': {'x1': 670, 'y1': 1990, 'x2': 730, 'y2': 2050}, }

'''
# coordinates with questions included
page_dist_coords = {'q1': {'x1': 0, 'y1': 260, 'x2': 855, 'y2': 1060},
                    'q2': {'x1': 855, 'y1': 260, 'x2': 1690, 'y2': 1060},
                    'q3': {'x1': 0, 'y1': 1060, 'x2': 855, 'y2': 2195},
                    'q4': {'x1': 855, 'y1': 1060, 'x2': 1699, 'y2': 2195},
                    'q5': {'x1': 0, 'y1': 0, 'x2': 855, 'y2': 1020},
                    'q6': {'x1': 855, 'y1': 0, 'x2': 1695, 'y2': 1020},
                    'q7': {'x1': 0, 'y1': 1020, 'x2': 855, 'y2': 1915},
                    'q8': {'x1': 855, 'y1': 1020, 'x2': 1695, 'y2': 1910},
                    'box': {'x1': 615, 'y1': 1995, 'x2': 730, 'y2': 2050},
                    'dg1': {'x1': 605, 'y1': 1990, 'x2': 665, 'y2': 2050},
                    'dg2': {'x1': 670, 'y1': 1990, 'x2': 730, 'y2': 2050}, }
# '''

# '''
# this is properly working code
# function to convert each page of the pdf to an image


def pdf_to_images(direc, pdf_path):

    # Convert the pdf to a list of images
    images = p2i.convert_from_path(pdf_path)

    # Iterate trough every image and save it to disk
    s = 1
    for i, image in enumerate(images):
        i = i % 2
        image_path = f'{os.path.splitext(pdf_path)[0]}_old/{direc}_response{math.floor(s)}_pg{i+1}.jpg'
        # print(image_path)
        s += 0.5
        # save only if the image is not present
        if not os.path.exists(image_path):
            image.save(image_path, 'JPEG')

# end_of_function


# Set the paths to the PDF files
pdf_names = {'4002'}    # we list all the pdf file names
pdf_paths = set()
for pdf_name in pdf_names:
    pdf_paths.add(pdf_name+'.pdf')

for pdf_path in pdf_paths:

    # create the directory withh pdf name if it does not exist
    direc = pdf_path.split('.pdf', 1)[0]
    ispresent = os.path.exists(direc)
    if not ispresent:
        os.makedirs(direc)

    # set the path of current pdf
    pdf_path = './' + pdf_path
    # print(direc, pdf_path)

    # calling the function pdf_to_images
    pdf_to_images(direc, pdf_path)
# '''


def get_cropped_image(img, which_img):

    x1 = page_dist_coords[which_img]['x1']
    y1 = page_dist_coords[which_img]['y1']
    x2 = page_dist_coords[which_img]['x2']
    y2 = page_dist_coords[which_img]['y2']

    # Crop the image using the defined coordinates
    sub_img = img.crop((x1, y1, x2, y2))
    return sub_img


# exit()
# '''
# open image
img = Image.open("./4002_old/4002_response2_pg2.jpg")
sub_img = get_cropped_image(img, 'dg1')
# Save the sub-image
sub_img.save("stuid.jpg")
# '''


# Load the low-resolution image
img = cv2.imread('stuid.jpg')

# # Upsample the image using bicubic interpolation
# upscaled = cv2.resize(img, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
# denoised = cv2.medianBlur(upscaled, 5)

# # Display the original and upscaled images
# cv2.imshow('Original', img)
# cv2.imshow('Upscaled', upscaled)
# cv2.imshow('denoised', denoised)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
# det_img = Image.open('stuid.jpg')
text = pt.image_to_string(img, config='--psm 10')

digit = text.strip()
# Print the recognized digit
print('Recognized string:', digit)
'''
