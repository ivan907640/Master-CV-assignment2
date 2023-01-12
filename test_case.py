from resize_image import *
from Image import load_img, save_img, Image, clamp_image
from filter_image import *


# nearest resize
def test_nn_resize_4x():
    img = load_img("data/dogsmall.jpg")
    resized = nearest_resize(img, img.w * 4, img.h * 4)
    save_img("out/nn_resize_4x.jpg", resized)


def test_nn_resize_adaptive():
    img = load_img("data/dog.jpg")
    resized = nearest_resize(img, 713, 467)
    save_img("out/nn_resize_adaptive.jpg", resized)



# bilinear resize
def test_bl_resize_4x():
    img = load_img("data/dogsmall.jpg")
    resized = bilinear_resize(img, img.w * 4, img.h * 4)
    save_img("out/bl_resize_4x.jpg", resized)


def test_bl_resize_adaptive():
    img = load_img("data/dog.jpg")
    resized = bilinear_resize(img, 713, 467)
    save_img("out/bl_resize_adaptive.jpg", resized)


# normalization
def test_l1_normalization():
    img = load_img("data/dog.jpg")
    img_l1 = l1_normalize(img)
    save_img("out/l1_normalization.jpg", img_l1)


# padding
def test_padding_image():
    img = load_img("data/dog.jpg")
    filter = make_box_filter(47)
    pad_img = padding_image(img, filter)
    save_img("out/padding_image.jpg", pad_img)


# convolution
def test_convolution():
    img = load_img("data/dog.jpg")
    filter = make_box_filter(7)
    pad_img = padding_image(img, filter)
    blur = convolve_image(pad_img, filter, True)
    clamp_image(blur)
    save_img("out/convolution_image.jpg", blur)


def test_convolution_no_preserve():
    img = load_img("data/dog.jpg")
    filter = make_box_filter(7)
    pad_img = padding_image(img, filter)
    blur = convolve_image(pad_img, filter, False)
    clamp_image(blur)
    save_img("out/convolution_no_preserve_image.jpg", blur)


# highpass filter
def test_highpass_filter():
    img = load_img("data/dog.jpg")
    filter = make_highpass_filter()
    pad_img = padding_image(img, filter)
    blur = convolve_image(pad_img, filter, False)
    clamp_image(blur)
    save_img("out/highpass_case.jpg", blur)



# sharpen filter
def test_sharpen_filter():
    img = load_img("data/dog.jpg")
    filter = make_sharpen_filter()
    pad_img = padding_image(img, filter)
    blur = convolve_image(pad_img, filter, True)
    clamp_image(blur)
    save_img("out/sharpen_case.jpg", blur)


# emboss filter
def test_emboss_filter():
    img = load_img("data/dog.jpg")
    filter = make_emboss_filter()
    pad_img = padding_image(img, filter)
    blur = convolve_image(pad_img, filter, True)
    clamp_image(blur)
    save_img("out/emboss_case.jpg", blur)



if __name__ == '__main__':
    #Case 1
    test_nn_resize_4x()

    #Case 2
    test_nn_resize_adaptive()

    #Case 3
    test_bl_resize_4x()

    #Case 4
    test_bl_resize_adaptive()

    #Case 4
    test_l1_normalization()

    #Case 5
    test_padding_image()

    #Case 6
    test_convolution()

    #Case 7
    test_convolution_no_preserve()

    #Case 8
    test_highpass_filter()

    #Case 9
    test_sharpen_filter()

    #Case 10
    test_emboss_filter()

    #Case 11
    test_convolution()

