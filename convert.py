import json
import os
import sys


def convert_links(input_file, output_file):
    with open(f"input/{input_file}", "r") as file:
        data = json.load(file)

    links = data["links"]
    new_links = []
    for link in links:
        source = link["source"]
        targets = link["targets"]
        for target in targets:
            new_links.append({"source": source, "target": target})

    data["links"] = new_links

    with open(f"data/{output_file}", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":

    if not os.path.exists("input"):
        print("Input folder not found")
        os.makedirs("input")
        sys.exit(0)

    input_files = []
    # read files from input folder
    for file in os.listdir("input"):
        if file.endswith(".json"):
            input_files.append(file)

    # if data folder not exists, create it
    if not os.path.exists("data"):
        os.makedirs("data")

    # convert each file
    for file in input_files:
        convert_links(file, file)
        print(f"Converted {file}")
