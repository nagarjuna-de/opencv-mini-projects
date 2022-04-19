## Import required libraries
import cv2
import os
import matplotlib.pyplot as plt

## Create a meme
## Load image
img_upload = input('Enter the image name with extension:')
uploaded_img = os.path.join(os.path.dirname(__file__), 'images', f'{img_upload}')

def show_img(description,image_name):
    image = cv2.imread(image_name)
    cv2.imshow(f'{description}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_img('your uploaded image', uploaded_img)

def spiderman_meme():
    img = cv2.imread(uploaded_img)
    copy_img = img.copy()
    cv2.putText(copy_img, 'Matplotlib RGB vs openCV BGR', (180,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),1)
    cv2.rectangle(copy_img,(120,5),(800,60),(0,0,0),3)
    cv2.putText(copy_img, 'You need to', (270,140), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0),1)
    cv2.putText(copy_img, 'be RED', (270,170), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0),1)
    cv2.putText(copy_img, 'You need to', (450,260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255),1)
    cv2.putText(copy_img, 'be BLUE', (450,290), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,255),1)
    return copy_img

copy_img = spiderman_meme()
cv2.imshow('final_meme', copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
