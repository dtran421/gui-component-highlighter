# gui-component-highlighter

## Background

The development environment uses a virtual environment (aliased as `venv`) to localize dependencies. This script makes use of the following packages:

- os
- shutil
- cv2 ([OpenCV](https://opencv.org/))

The script is split into 3 files: `main.py`, `xml_script.py`, and `img_script`. The input data files are stored in the provided directory under the alias `Programming-Assignment-Data`.


### Main Script

The `main.py` script is responsible for the high-level logic of the program. It retrieves the program's folder path and locates the `Programming-Assignment-Data` folder within. It then goes through all of the XML files and processes them using the `xml_script.py` script. Using the metadata obtained from the XML files, it then uses the `img_script.py` script to annotate the screenshots accordingly. 


### XML Script

The `xml_script.py` script contains a function, `process_file`, that is responsible for opening the XML file, reading in the lines, and retrieving leaf nodes based on their unique tag pattern. In other words, nodes that have children have an opening and closing tag, which might look like:

```xml
    <node>
        ...
    </node>
```

Since leaf nodes don't have children, we don't need a separate opening and closing tag and can instead express the node in a singular tag with two angular brackets and a forward slash, as can be seen:

```xml
    <node />
```

### Image Script

The `img_script.py` script contains a function, `modify_image`, that copies a given image to the output directory, draws yellow rectangles to highlight components using their bounding boxes, and saves the annotated image.

Since the XML files contain metadata relating to each component, each node must contain information on its bounding box since it's fixed within the given screen and must know its precise location to be displayed. Therefore, these bounding box coordinates can be leveraged to draw the highlighting rectangles surrounding leaf components.

I used the OpenCV package since it provides simple utility functions to draw shapes onto images and overwrite (thus saving edited) images.


## Program Execution

### Starting Up the Virtual Environment

To launch the virtual environment, run the following command:

```bash
    source venv/bin/activate
```

It should have all package dependencies installed. If not, simply run the following command to install OpenCV:

```bash
    pip install opencv-python
```

### Running the Script

To run the script, simply execute the following command:

```bash
    venv/bin/python main.py
```

Make sure you run the script using the virtual environment and not the global Python installation on your machine, or else it won't have OpenCV installed. If you want to install OpenCV directly for your global Python installation, then feel free to do so and run the script as you normally run other Python programs.


## Output

The outputted set of annotated screenshots are stored in the `/output` folder. There are 7 screenshots that correspond to the 7 screens provided by the assignment data.
