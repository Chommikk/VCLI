from stegano import lsb

def hide_message(text, image):
    file = lsb.hide(image, text)
    file.save("hid" + image)
    return ("hid" + image)


def get_message(image):
    return(lsb.reveal(image))

