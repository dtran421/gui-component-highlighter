def process_file(__filepath):
    with open(__filepath) as file:
        lines = [l.strip() for l in file.readlines()]
        if len(lines) == 1:
            lines = [l + ">" for l in lines[0].strip().split(">")]

        leaves = []
        for l in lines:
            if l[0] == "<" and l[-2:] == "/>":
                leaves.append(l)

        return leaves
