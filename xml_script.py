from typing import List


def process_file(__filepath: str) -> List[str]:
    """
    Opens xml file, reads in lines, and retrieves leaf nodes
    """
    with open(__filepath) as file:
        # read in all xml lines and remove whitespace,
        # files can vary in formatting, some are only 1 line,
        # others are tabbed properly with newlines
        lines = [l.strip() for l in file.readlines()]
        # split up lines of "condensed" xml files
        if len(lines) == 1:
            lines = [l + ">" for l in lines[0].strip().split(">")]

        leaves = []
        for l in lines:
            # retrieve leaf nodes based on component formatting
            # components that have no children must end in /> rather than >
            if l[0] == "<" and l[-2:] == "/>":
                leaves.append(l)

        return leaves
