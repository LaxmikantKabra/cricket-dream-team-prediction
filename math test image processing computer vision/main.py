import os
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pdf2image.pdf2image as p2i
from PIL import Image
from keras.models import load_model


# defined coordinates of the sub-images
# coordinates with questions not included
page_dist_coords = {'q1': {'x1': 0, 'y1': 348, 'x2': 850, 'y2': 1060},
                    'q2': {'x1': 860, 'y1': 335, 'x2': 1690, 'y2': 1060},
                    'q3': {'x1': 0, 'y1': 1176, 'x2': 850, 'y2': 2195},
                    'q4': {'x1': 850, 'y1': 1105, 'x2': 1690, 'y2': 2195},
                    'q5': {'x1': 0, 'y1': 335, 'x2': 855, 'y2': 1020},
                    'q6': {'x1': 860, 'y1': 315, 'x2': 1685, 'y2': 1020},
                    'q7': {'x1': 0, 'y1': 1138, 'x2': 855, 'y2': 1915},
                    'q8': {'x1': 858, 'y1': 1130, 'x2': 1685, 'y2': 1915},
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
'''


def get_cropped_image(img, which_img):

    img = img[1]
    # because model is trained on grayscale channel images
    img_gray = img.convert('L')
    x1 = page_dist_coords[which_img]['x1']
    y1 = page_dist_coords[which_img]['y1']
    x2 = page_dist_coords[which_img]['x2']
    y2 = page_dist_coords[which_img]['y2']

    # Crop the image using the defined coordinates
    # print(img)
    sub_img = img_gray.crop((x1, y1, x2, y2))
    return sub_img


# '''
# classify image to student_id digits and return string
model1 = load_model('./MNIST_keras_CNN.h5')


def predict_student_id(img):

    sub_img1 = get_cropped_image(img, 'dg1')
    sub_img2 = get_cropped_image(img, 'dg2')

    d1, d2 = sub_img1.resize((28, 28)), sub_img2.resize((28, 28))
    d1, d2 = np.array(d1), np.array(d2)
    d1, d2 = d1.reshape(1, 28, 28, 1), d2.reshape(1, 28, 28, 1)
    d1, d2 = d1.astype('float32'), d2.astype('float32')
    d1 /= 255
    d2 /= 255

    # Use the model to make a prediction
    pred1 = model1.predict(d1)
    pred2 = model1.predict(d2)

    # Print the predicted label
    d1_pred_label = np.argmax(pred1)
    d2_pred_label = np.argmax(pred2)
    d1_pred_label, d2_pred_label = str(d1_pred_label), str(d2_pred_label)
    label = d1_pred_label+d2_pred_label
    return label

# end of function
# '''


# '''
# this is properly working code
# function to convert each page of the pdf to an image


def pdf_to_images(direc, pdf_path):

    # Convert the pdf to a list of images
    imgs = p2i.convert_from_path(pdf_path)

    flag = True
    student_id = '00'
    # Iterate through images in reverse direction
    for img in enumerate(reversed(imgs)):
        if flag == True:
            student_id = predict_student_id(img)
            start, end = 5, 9

            img_name = direc + '_' + student_id + '_digits' + '.jpg'
            sub_img = get_cropped_image(img, 'box')
            image_path = './'+direc + '/' + img_name
            # if not os.path.exists(image_path):
            sub_img.save(image_path, 'JPEG')

        else:
            start, end = 1, 5

        for que_num in range(start, end, 1):
            img_name = direc + '_' + student_id + '_' + str(que_num) + '.jpg'
            param = 'q'+str(que_num)
            sub_img = get_cropped_image(img, param)
            image_path = './'+direc + '/' + img_name
            # if not os.path.exists(image_path):
            sub_img.save(image_path, 'JPEG')

        flag = not flag
    return

    # Iterate through every image and save it to disk
    # s = 1
    # for i, image in enumerate(reversed(imgs)):
    #     i = i % 2
    #     image_path = f'{os.path.splitext(pdf_path)[0]}/{direc}_response{math.floor(s)}_pg{i+1}.jpg'
    #     s += 0.5
    #     # save only if the image is not present
    #     if not os.path.exists(image_path):
    #         image.save(image_path, 'JPEG')

# end_of_function


pdf_names = {'4002'}    # we list all the pdf file names

# Set the paths to the PDF files
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
