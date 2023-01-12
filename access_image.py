import numpy as np



def pixel_address(img, i, j, k):
    ##TODO: calculate and return the index
    return j + i*img.w + k*img.w*img.h



def copy_image(Image_this, Image_from):

    h, w, c = Image_from.h, Image_from.w, Image_from.c
    #allocating data for the new image
    Image_this.data = np.zeros((h*w*c), np.float16)
    Image_this.h, Image_this.w, Image_this.c = h, w, c

    #TODO: copy the data
    #You might use 'copy' in numpy array
    Image_this.data = Image_from.data.copy()
