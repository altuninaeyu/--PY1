import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",", new_line="\n") -> list[dict]:

    with open(filename, "r") as f:
        header = f.readline().strip(new_line).split(delimiter)
        data = [line.strip(new_line).split(delimiter) for line in f]

    return [{header[i]:row[i] for i in range(0,len(row))} for row in data]

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
