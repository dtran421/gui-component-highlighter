import os

from xml_script import process_file
from img_script import modify_image


# folder path
__dirpath = os.getcwd()
__dirname = f"{__dirpath}/Programming-Assignment-Data"

# go through directory
for filename in os.listdir(__dirname):
    # process xml files first, then corresponding image files
    if filename.endswith(".xml"):
        __filepath = f"{__dirname}/{filename}"
        components = process_file(__filepath)

        modify_image(
            __dirpath, f"{__filepath[:-4]}.png", f"{filename[:-4]}.png", components
        )
