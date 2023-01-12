from locale import ABDAY_1
from matplotlib.colors import hex2color
from Image import Image

def nearest_resize(img, w, h):
    source = img
    target = Image(h, w, img.c)
    ## note: access pixel should input [h_coord, w_coord, c_coord], and simply use int() to get integer number, not round()
    ## TODO: use source pixel value to fill target pixel value
    
    ## Get ratio for resize
    w_ratio = w/source.w ; h_ratio = h/source.h
    w_ratio_array = []; h_ratio_array = []; 

    ## Caulculate the integer index of each target pixel
    ## +0.5 and int to prevent shifting
    for j in range(w):
        w_ratio_array.append(int((j+0.5)/w_ratio))
    for i in range(h):
        h_ratio_array.append(int((i+0.5)/h_ratio))

    ## Read source pixel by index
    for k in range(target.c):
        for j in range(w):
            for i in range(h):
                target[i,j,k] = source[h_ratio_array[i],w_ratio_array[j],k] 

    return target

def bilinear_resize(img, w, h):
    source = img
    target = Image(h, w, img.c)
    ## note: access pixel should input [h_coord, w_coord, c_coord], and simply use int() to get integer number, not round()
    ## TODO: use source pixel value to fill target pixel value

    ## Import numpy for ceil and floor
    import numpy as np
    ## Get ratio for resize
    ## ratio -1 as both sides -0.5
    w_ratio = (w-1)/(source.w-1) ; h_ratio = (h-1)/(source.h-1)
    w_ratio_array = []; h_ratio_array = []; 

    ## Caulculate the float index of each target pixel
    ## Rounding to prevent integer get ceiling 
    for j in range(w):
        w_ratio_array.append(round(j/w_ratio,10))
    for i in range(h):
        h_ratio_array.append(round(i/h_ratio,10))
    
    for k in range(target.c):
        for j in range(w):
            for i in range(h):
                # Calculate height and width to 4 points
                height1 = (h_ratio_array[i]-np.floor(h_ratio_array[i]))
                height2 = 1-height1
                width1  = (w_ratio_array[j]-np.floor(w_ratio_array[j]))
                width2  = 1-width1
                # Calculate ratio of each point
                ratio1 = (1-height1)*(1-width1)
                ratio2 = (1-height1)*(1-width2)
                ratio3 = (1-height2)*(1-width1)
                ratio4 = (1-height2)*(1-width2)
                # Calculate the final value for target pixel
                value1 = ratio1 * source[int(np.floor(h_ratio_array[i])),int(np.floor(w_ratio_array[j])),k] 
                value2 = ratio2 * source[int(np.floor(h_ratio_array[i])),int(np.ceil(w_ratio_array[j])),k] 
                value3 = ratio3 * source[int(np.ceil(h_ratio_array[i])) ,int(np.floor(w_ratio_array[j])),k] 
                value4 = ratio4 * source[int(np.ceil(h_ratio_array[i])) ,int(np.ceil(w_ratio_array[j])),k] 
                target[i,j,k] = value1+value2+value3+value4
                
    return target