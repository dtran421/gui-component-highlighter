import os

from xml_script import process_file
from img_script import modify_image

if __name__ == "__main__":
    """
    Loops over Programming-Assignment-Data directory to find XML files, obtains leaf components, then
    annotates images according to their bounding boxes
    """
    # directory path
    __dirpath = os.getcwd()
    __dirname = f"{__dirpath}/Programming-Assignment-Data"

    # go through directory
    for filename in os.listdir(__dirname):
        # process xml files first, then corresponding image files
        if filename.endswith(".xml"):
            __filepath = f"{__dirname}/{filename}"
            # obtain leaf components from xml
            components = process_file(__filepath)

            # annotate leaf components and output images
            modify_image(
                __dirpath, f"{__filepath[:-4]}.png", f"{filename[:-4]}.png", components
            )
