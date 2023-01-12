import cv2
from access_image import *


class Image():
    def __init__(self, height = 0, width = 0, channel = 0):
        if height >= 0 and width >= 0 and channel >= 0:
            pass
        else:
            raise ValueError("Invalid image sizes")

        self.h, self.w, self.c = height, width, channel
        self.data = np.zeros((self.h*self.w*self.c), np.float16)


    def __getitem__(self, item):
        i, j, k = item
        return self.data[pixel_address(self, i, j, k)]


    def __setitem__(self, key, value):
        i, j, k = key
        self.data[pixel_address(self, i, j, k)] = value


    def myassign(self, Image_from):
        self.h, self.w, self.c = 0, 0, 0
        copy_image(self, Image_from)


def clamp_image(img):
    ##TODO: clamp all the pixels in all channel to be between 0 and 1
    for k in range(img.c):
        for i in range(img.h):
            for j in range(img.w):
                v = img[i, j, k]
                if (v < 0.0):
                    v = 0.0
                if (v > 1.0):
                    v = 1.0
                img[i, j, k] = v


def load_img(path, GRAY=False):
    if GRAY:
        data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)/255.0
        data = data[:,:,None].astype(np.float16)
    else:
        data = cv2.imread(path)### opencv is BGR
        data = data.astype(np.float16) / 255
    data = data[..., ::-1] ## change to RGB
    h, w, c = data.shape
    img = Image(h, w, c)
    for k in range(c):
        for j in range(h):
            for i in range(w):
                index = i + w * j + w * h * k
                img.data[index] = data[j, i, k]
    return img


def save_img(savepath, img):
    h, w, c = img.h, img.w, img.c
    data = np.zeros((h, w, c))
    for k in range(c):
        for j in range(h):
            for i in range(w):
                index = i + w * j + w * h * k
                data[j, i, k] = img.data[index]
    # data is RGB
    data = data[..., ::-1] ## change to BGR to fit the opencv format
    cv2.imwrite(savepath, (np.round(data*255)).astype(np.uint8))