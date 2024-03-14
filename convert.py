import json
import os
import sys


# convert
# {"source": "r0", "targets": ["c50", "c51", "c64", "c131", "c50", "c51", "c52", "c104", "c50", "c51", "c81", "c121", "c50", "c51", "c61", "c147"]},
# to
# {"source": "r0", "target": "c50"},
# {"source": "r0", "target": "c51"},
# {"source": "r0", "target": "c64"},
# ...
# dont touch other data
# file construct
# {
#     "nodes": [
#         {
#           "id": "r{ID перекрестка}",
#           "name": "r{ID перекрестка}",
#           "val": 1 // 1 - просто комната, 2 - старт, 3 - флаг
#         },
#         {
#           "id": "с{ID коридора}",
#           "name": "с{ID коридора}",
#           "val": 1
#         },
#         ...
#     ],
#     "links": [
#         {
#             "source": "{ID #1}",
#             "targets": ["{ID #2}", "{ID #3}", "{ID #4}", ...]
#         },
#         ...
#     ]
# }
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

    with open(f"output/{output_file}", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    input_files = []
    # read files from input folder
    for file in os.listdir("input"):
        if file.endswith(".json"):
            input_files.append(file)

    # if output folder not exists, create it
    if not os.path.exists("output"):
        os.makedirs("output")

    # convert each file
    for file in input_files:
        convert_links(file, file)
        print(f"Converted {file}")
