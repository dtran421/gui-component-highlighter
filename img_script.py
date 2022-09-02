import os
import shutil
from typing import List
import cv2


def modify_image(
    __dirpath: str, __filepath: str, img_filename: str, components: List[str]
) -> None:
    """
    Copies image to output directory, draws yellow highlighting rectangles using
    bounding boxes of components, and saves the annotated image
    """
    # define output path and creates directory if it doesn't exist
    out_dir = __dirpath + "/output"
    os.makedirs(out_dir, exist_ok=True)

    # copy image to output directory and reads image data into opencv
    shutil.copy(__filepath, out_dir)
    __imgpath = f"{out_dir}/{img_filename}"
    img = cv2.imread(__imgpath)

    for comp in components:
        # retrieve bounds attribute from component
        bounds = None
        for attr in comp.split(" "):
            if "bounds" in attr:
                bounds = attr

        # parse bounding box data from attribute string
        bounding_box = bounds[bounds.index("=") + 1 :][1:-1]
        tl_p, br_p = [p.split(",") for p in bounding_box[1:-1].split("][")]

        xt, yt = [int(i) for i in tl_p]
        xb, yb = [int(i) for i in br_p]

        # use opencv to draw yellow rectangle highlighting component
        # using bounding box data
        cv2.rectangle(img, (xt, yt), (xb, yb), (0, 225, 255), 8)

    """ 
    # [DEBUG]
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    """

    # save image using opencv
    cv2.imwrite(__imgpath, img)
