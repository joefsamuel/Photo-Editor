# With help by Professor D.L. Bailey (Carleton University)

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

#if __name__ == "__main__":

 #   img = get_image()
  #  show(img)

thshld = 0
image_chk = False
# Menu Interface
if __name__ == "__main__":
    done = False
    while not done:
        print("Choose a command from below and enter it's inital to select:")
        print("L) Load Image")
        print("N) Negative")
        print("G) Grayscale")
        print("P) Posterize")
        print("S) Sepia tint")
        print("E) Edge detect")
        print ("Q) Quit")
        prompt = ("Enter your choice: ")

        answer = str(input(prompt))


        if answer == "L":
            print("You have choosen to load an image")
            img = get_image()
            show(img)
            print("Image choosen")
            image_chk = True
        elif answer == "N":
            print("You have choosen to use the negative filter")
            if image_chk == True:
                negtive_filter = negative(img)
                show (img)
            else:
                print ("No Image Loaded!")
        elif answer == "G":
            if image_chk == True:
                print("You have choosen the Grayscale filter")
                wgrayscale_filter = weighted_grayscale(img)
                show(img)
            else:
                print ("No Image Loaded!")
        elif answer == "P":
            if image_chk == True:
                print("You have choosen to use the Posterize filter")
                posterize_filter = posterize(img)
                show (img)
            else:
                print ("No Image Loaded!")
        elif answer == "S":
            if image_chk == True:
                print("You have choosen to use the sepia filter")
                sepia_filter = sepia_tint(img)
                show (img)
            else:
                print ("No Image Loaded!")
        elif answer == "E":
            if image_chk == True:
                print("You have choosen to use the edge detect filter")
                prompt = ("Enter the threshold: ")
                thshld = int(input(prompt))
                detect_edges_filter = detect_edges_better(img, thshld)
                show (img)
            else:
                print ("No Image Loaded!")
        elif answer == "Q":
            print("Quiting the program")
            done = True
        else:
           print("No such command")
