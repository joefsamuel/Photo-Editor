# With help by Professor D.L. Bailey (Carleton University)

from Cimpl import *

def grayscale(img):
    """ (Cimpl.Image) -> None

    Converts the specified picture into a grayscale image.

    >>> image = load_image(choose_file())
    >>> grayscale(image)
    >>> show(image)
    """

    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Uses the shade of gray that has the same brightness as the pixel's
        # original color.

        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)

        set_color(img, x, y, gray)

def negative(img):
    """ (Cimpl.Image) -> None

        Converts the specified picture into a inverted-colour image.

        >>> image = load_image(choose_file())
        >>> negative(image)
        >>> show(image)
        """
    for pixel in img:
        x, y, col = pixel
        r, g, b = col
        col = create_color(255-r, 255-g, 255-b)
        set_color(img, x, y, col)




def weighted_grayscale(img):
    """ (Cimpl.Image) -> None

    Converts the specified picture into an acurate grayscale image.

    >>> image = load_image(choose_file())
    >>> weighted_grayscale(image)
    >>> show(image)
    """

    for pixel in img:
        x, y, col = pixel
        r, g, b = col

        # Uses the shade of gray that has the same brightness as the pixel's
        # original color.

        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)

        set_color(img, x, y, gray)

def solarize(img, threshold):
    """ (Cimpl.Image) -> None

    Solarize the specified image.

    >>> image = load_image(choose_file())
    >>> solarize(image,128)
    >>> show(image)
    """

    for x, y, col in img:
        red, green, blue = col

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(img, x, y, col)

def black_and_white(img):
    """ (Cimpl.Image) -> None

    Convert the specified image to a black-and-white (two-tone) image.

    >>> image = load_image(choose_file())
    >>> black_and_white(image)
    >>> show(image)
    """

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3

        if brightness < 128:
            set_color(img, x, y, black)
        else:
            set_color(img, x, y, white)


def black_and_white_and_gray(img):
    """ (Cimpl.Image) -> None

    Convert the specified image to a black-and-white-and-gray
    (three-shade) image.

    >>> image = load_image(choose_file())
    >>> black_and_white_and_gray(image)
    >>> show(image)
    """

    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    for x, y, col in img:
        red, green, blue = col

        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(img, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(img, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(img, x, y, white)

def extreme_contrast(img):
    """(Cimpl.image) -> None

    Modifies img, maximizing the contrast between the light and dark pixels.

    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(image)
    """


    for x, y, col in img:
            red, green, blue = col

            if red < 128:
                red=0
            else:
                red=255
            if green < 128:
                green=0
            else:
                green=255
            if blue < 128:
                blue=0
            else:
                blue=255


def sepia_tint(img):
    """(Cimpl.image) -> None

    Converts the specified image to sepia tones.

    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """

    grayscale(img)

    for x, y, col in img:
        red, green, blue = col


        if red < 63:
            blue = blue * 0.9
            red = red * 1.1
        elif red < 191 :
            blue = blue * 0.85
            red = red * 1.15
        else:
            blue = blue * 0.93
            red = red * 1.08


def _adjust_component(amount):
    """ (int) -> int

    Divides the range 0..255 into 4 equal size quadrants, and return the midpoint of the quadrant in which the specified amount lies.

    >>> _adjust_component(10)
    31
    >>> _adjust component(85)
    95
    """

    if amount < 63:
        amount = 31
    elif amount < 127 :
        amount = 95
    elif amount < 191 :
        amount = 159
    else:
        amount = 223
    return amount


def posterize(img):
    """(Cimpl.image) -> None

    "Posterize" the specified image.

    >>> image = load_image(choose_file())
    >>> posterize(image)
    >>> show(image)
    """

    for x, y, col in img:
            red, green, blue = col
            red = _adjust_component(red)
            green = _adjust_component(green)
            blue = _adjust_component(blue)

def simplify(img):
    """(Cimpl.image) -> None

    Modifies img so that each pixel is white, black, red, green or blue. Very bright pixels are changed to white. Very dark pixels are changed to black. All other pixels are changed to red, green or blue, depending on which component is the largest.

    >>> image = load_image(choose_file())
    >>> simplify(image)
    >>> show(image)
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)
    Colour_1 = create_color(255,0,0)
    Colour_2 = create_color(0,255,0)
    Colour_3 = create_color(0,0,255)

    for x, y, col in img:
         r, g, b = col
         if r > 200 and b > 200 and g > 200:
             set_color(img, x, y, white)
         elif r < 50 and b < 50 and g < 50:
                 set_color(img, x, y, black)
         elif r > g and r > b:
                set_color(img, x, y, Colour_1)
         elif g > r and g > b:
                set_color(img, x, y, Colour_2)
         else:
             set_color(img, x, y, Colour_3)


def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a new image that is a blurred copy of the image bound to source.

    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)
    """

    target = copy(source)

    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @(x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red ) // 5

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green ) // 5

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue ) // 5

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def detect_edges(img, threshold):
    """(Cimpl.image, float) -> None

    Modifies the specified image using edge detection.
    An edge is detected when a pixel's brightness differs from that of its neighbour by an amount that is greater then the specified threshold.

    >>> image = load_image(choose_file())
    >>> detect_edges(image)
    >>> show(image)
    """

    for y in range(0, get_height(img) - 1):
        for x in range(0, get_width(img)):
            top_red, top_green, top_blue = get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)

            top_pixels = (top_red + top_green + top_blue)//3
            down_pixels = (bottom_red + bottom_green + bottom_blue)//3
            bContrast = top_pixels - down_pixels
            contrast = abs(bContrast)

            if contrast>threshold:
                New_color_img = create_color(0,0,0)
                set_color(img,x,y,New_color_img)

            else:
                New_color_img2 = create_color(255,255,255)
                set_color(img,x,y,New_color_img2)


def detect_edges_better(img, threshold):
    """(Cimpl.image, float) -> None

    Modifies the specified image using edge detection.
    An edge is detected when a pixel's brightness differs from that of its neighbour by an amount that is greater than the specified threshold.

    >>> image = load_image(choose_file())
    >>> detect_edges_better(image)
    >>> show(image)
    """

    for y in range(0, get_height(img) - 1):
        for x in range(0, get_width(img) - 1):
            top_red, top_green, top_blue = get_color(img, x, y)
            bottom_red, bottom_green, bottom_blue = get_color(img, x, y + 1)
            right_red, right_green, right_blue = get_color(img, x + 1, y)

            top_pixels = (top_red + top_green + top_blue)//3
            right_pixels = (right_red + right_green + right_blue)//3
            down_pixels = (bottom_red + bottom_green + bottom_blue)//3

            bContrast = top_pixels - down_pixels - right_pixels
            contrast = abs(bContrast)

            if contrast>threshold:
                New_color_img = create_color(0,0,0)
                set_color(img,x,y,New_color_img)

            else:
                New_color_img2 = create_color(255,255,255)
                set_color(img,x,y,New_color_img2)

def blur_better(source):
    """ (Cimpl.Image) -> Cimpl.Image

    Returns a new image that is a blurred copy of the image bound to source.

    original = load_image(choose_file())
    blurred2 = blur_better(original)
    show(original)
    show(blurred)
    """

    target = copy(source)

    sred = 0
    sgreen = 0
    sblue = 0

    for y in range(1, get_height(source)-2):
        for x in range(1, get_width(source)-2):
            red, green, blue = get_color(source, x, y)
            sred = sred + red
            sgreen = sgreen + green
            sblue = sblue + blue



            # Average the red components of the five pixels
            new_red = sred//5

            # Average the green components of the five pixels
            new_green = sgreen//5

            # Average the blue components of the five pixels
            new_blue = sblue//5

            # Blur the pixel @(x, y) in the copy of the image
            new_color = create_color(new_red, new_green, new_blue)
            set_color(target, x, y, new_color)

    return target


def flip(img):
    """(Cimpl.Image) -> None

    Flip the specified image aorund an imaginary vertical line drawn through the midpoint of the image.

    >>> image = load_image(choose_file())
    >>> flip(image)
    >>> show(image)
    """


    for y in range(0, get_height(img)-1):
        for x in range(0, get_width(img)):
                red, green, blue = get_color(img, x, y)
                Ncol = create_color(red, green, blue)
                oppx = get_width(img) - 1 - x
                set_color(img,oppx,y, Ncol)
