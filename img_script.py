import os
import shutil
import cv2


def modify_image(__dirpath, __filepath, img_filename, components):
    out_dir = __dirpath + "/output"
    os.makedirs(out_dir, exist_ok=True)

    shutil.copy(__filepath, out_dir)
    __imgpath = f"{out_dir}/{img_filename}"
    img = cv2.imread(__imgpath)

    for comp in components:
        bounds = None
        for attr in comp.split(" "):
            if "bounds" in attr:
                bounds = attr

        bounding_box = bounds[bounds.index("=") + 1 :][1:-1]
        tl_p, br_p = [p.split(",") for p in bounding_box[1:-1].split("][")]

        xt, yt = [int(i) for i in tl_p]
        xb, yb = [int(i) for i in br_p]

        cv2.rectangle(img, (xt, yt), (xb, yb), (0, 225, 255), 8)

    cv2.imshow("image", img)
    """ cv2.waitKey(0)
    cv2.destroyAllWindows() """

    cv2.imwrite(__imgpath, img)
