## Import required libraries
import cv2
import os
import matplotlib.pyplot as plt

# Detect the QR code in the image using QRCodeDetector()   

## Load the image
img_upload = input('Enter the image name with extension:')
uploaded_img = os.path.join(os.path.dirname(__file__), 'images', f'{img_upload}')

def show_img(description,image_name):
    image = cv2.imread(image_name)
    cv2.imshow(f'{description}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_img('your uploaded image', uploaded_img)

def qr_code_detector():
    img = cv2.imread(uploaded_img)
    qr_data, point, straight_qr = cv2.QRCodeDetector().detectAndDecode(img)
    return img, qr_data, point, straight_qr

img, qr_data, points, straight_qr = qr_code_detector()

def image_qr_code():
    global points
    if len(points)>0:
        print('QR Code Detected')
        print('Decoded QR :', qr_data)
        points = points[0]
        for i in range(len(points)):
            pt1 = [int(val) for val in points[i]]
            pt2 = [int(val) for val in points[(i + 1) % 4]]
            cv2.line(img, pt1, pt2, color=(255, 0, 0), thickness=3)

        cv2.imshow('Highlighted QR code Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        print('No QR Code found')

image_qr_code()

#### Code for only qr code image from the uploaded image using QRCodeDetector()

# only_qr = cv2.resize(straight_qr, (400,400))
# cv2.imshow('only QR code',only_qr)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




