from PIL import Image, ImageTk

def import_image(addres='resources/gui/pictures/pid.png', size=600, for_tk=True):
    def re_sizer(image, max=size):
        width, height = image.size

        if height > width:
            scale = height / max
            width = width / scale
            height = height / scale
        else:
            scale = width / max
            width = width / scale
            height = height / scale
        return int(width), int(height)

    my_img = Image.open(addres)
    width, height = re_sizer(my_img)

    my_img = my_img.resize((width, height), Image.ANTIALIAS)

    my_img = resize_image(image=my_img, max_side_size=size)

    if for_tk:
        image = ImageTk.PhotoImage(my_img)
    else:
        image = my_img
    return image

def resize_image(image, max_side_size):
    '''function is resizing image by his longest side to "max_side_size"
    other side is proportional to original'''

    width, height = image.size

    if height > width:
        scale = height / max_side_size
        width = width / scale
        height = height / scale
    else:
        scale = width / max_side_size
        width = width / scale
        height = height / scale

    width = int(width)
    height = int(height)

    return image.resize((width, height))