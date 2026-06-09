import pandas as pd

def parse_label_file(label_path):
    objects = []

    with open(label_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()

        objects.append({
            "type": parts[0],
            "truncated": float(parts[1]),
            "occluded": int(parts[2]),
            "xmin": float(parts[4]),
            "ymin": float(parts[5]),
            "xmax": float(parts[6]),
            "ymax": float(parts[7]),
        })

    return pd.DataFrame(objects)
