#### Importing libraries
import cv2
import os
import matplotlib.pyplot as plt

#### Loading the images

# Green screen image
img_gs = input('Enter the green screen image name with extension:')
gs_img = os.path.join(os.path.dirname(__file__), 'images', f'{img_gs}')

## Background image
img_bg = input('Enter the background image name with extension:')
bg_img = os.path.join(os.path.dirname(__file__), 'images', f'{img_bg}')


def green_screen():
    ### Working with green screen image

    img = cv2.imread(gs_img)
    rgb_h = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv_h = cv2.cvtColor(rgb_h, cv2.COLOR_RGB2HSV)
    ## Masking green screen
    lower_bounds = (45, 100, 20)
    upper_bounds = (72, 255, 255)

    mask = cv2.inRange(hsv_h, lower_bounds, upper_bounds)

    masked_h = hsv_h.copy()
    masked_h[mask!=0] = [0,0,0]

    ### Working with background 
    back_img = cv2.imread(bg_img)
    rgb_bg = cv2.cvtColor(back_img, cv2.COLOR_BGR2RGB)
    rgb_bg = cv2.resize(rgb_bg, (img.shape[1], img.shape[0]))
    hsv_bg = cv2.cvtColor(rgb_bg, cv2.COLOR_RGB2HSV)
    hsv_bg[mask == 0] = [0,0,0]


    #getting full image
    full_image = masked_h + hsv_bg
    full_image = cv2.cvtColor(full_image, cv2.COLOR_HSV2BGR)

    return full_image

full_image = green_screen()

cv2.imshow('full image', full_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

