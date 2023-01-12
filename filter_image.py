from Image import Image


def l1_normalize(img):
    ret = Image(img.h, img.w, img.c)
    for k in range(img.c):
        for j in range(img.w):
            for i in range(img.h):
                ## Fill all with 1 and normalize
                ret[i,j,k] = 1/(img.w*img.h)

    return ret

class make_box_filter(object):
    def __init__(self, kernel_size):
        if kernel_size % 2 == 0:
            raise ValueError("kernel size needs to be odd")
        self.kernel = Image(kernel_size, kernel_size, 1)
        self.h = self.kernel.h
        self.w = self.kernel.w
        self.c = self.kernel.c

        #Create the filter image
        self.ret = Image(self.h, self.w, self.c)
        for j in range(self.ret.w):
            for i in range(self.ret.h):
                ## Fill all with 1 and normalize
                self.ret[i,j,0]=1/(self.ret.w*self.ret.h)

    def __call__(self, local):
        out = 0
        return out


def padding_image(img, filter):
    stride = 1
    padding = int((filter.h - stride)/2)
    ret = Image(img.h+padding*2, img.w+padding*2, img.c)
    
    for k in range(ret.c):
        for j in range(padding,img.w+padding):
            for i in range(padding,img.h+padding):
                ret[i,j,k] = img[i-padding,j-padding,k]

    return ret

def convolve_image(img, filter, preserve):
    if filter.c != 1:
        raise ValueError("filter kernel should only have 1 channel")
    
    #For preserve as True
    #Loop cover the filter image for each pixel and add up as 3 channels
    if preserve == True:
        ret = Image(img.h-filter.h +1, img.w-filter.w +1, img.c)
        for k in range(ret.c):
            for j in range(ret.w):
                for i in range(ret.h):
                    value = 0
                    for n in range(filter.w):
                        for m in range(filter.h):
                            temp = filter.ret[m,n,0]*img[m+i,n+j,k]
                            value = value+temp
                    ret[i,j,k] = value
    
    #For preserve as True
    #Loop cover the filter image for each pixel and add up as 1 channel
    if preserve == False:
        ret = Image(img.h-filter.h +1, img.w-filter.w +1, 1)
        for j in range(ret.w):
                for i in range(ret.h):
                    value = 0
                    for k in range(img.c):
                        for n in range(filter.w):
                            for m in range(filter.h):
                                temp = filter.ret[m,n,0]*img[m+i,n+j,k]
                                value = value+temp
                    ret[i,j,0] = value

    return ret


class make_highpass_filter(object):
    def __init__(self):
        self.kernel = Image(3, 3, 1)

        self.h = self.kernel.h
        self.w = self.kernel.w
        self.c = self.kernel.c

        #Create High Pass Filter
        self.ret = Image(self.h, self.w, self.c)
        self.ret[0,0,0] = self.ret[0,2,0] = self.ret[2,0,0] = self.ret[2,2,0] = 0
        self.ret[1,0,0] = self.ret[0,1,0] = self.ret[2,1,0] = self.ret[1,2,0] = -1
        self.ret[1,1,0] = 4
                
    def __call__(self, local):
        out = 0
        return out

class make_sharpen_filter(object):
    def __init__(self):
        self.kernel = Image(3, 3, 1)

        self.h = self.kernel.h
        self.w = self.kernel.w
        self.c = self.kernel.c

        #Create Sharpen Filter
        self.ret = Image(self.h, self.w, self.c)
        self.ret[0,0,0] = self.ret[0,2,0] = self.ret[2,0,0] = self.ret[2,2,0] = 0
        self.ret[1,0,0] = self.ret[0,1,0] = self.ret[2,1,0] = self.ret[1,2,0] = -1
        self.ret[1,1,0] = 5

    def __call__(self, local):
        out = 0
        return out


class make_emboss_filter(object):
    def __init__(self):
        self.kernel = Image(3, 3, 1)

        self.h = self.kernel.h
        self.w = self.kernel.w
        self.c = self.kernel.c

        #Create Emobss Filter
        self.ret = Image(self.h, self.w, self.c)
        self.ret[0,0,0] = -2
        self.ret[1,0,0] = self.ret[0,1,0] = -1
        self.ret[2,0,0] = self.ret[0,2,0] = 0
        self.ret[1,1,0] = self.ret[2,1,0] = self.ret[1,2,0] = 1
        self.ret[2,2,0] = 2

    def __call__(self, local):
        out = 0
        return out