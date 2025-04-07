import os, json
from ast import literal_eval

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    allowed_keys = {"unordered_numbers",  "ordered_numbers", "dna_sequence"}
    if field not in allowed_keys:
        return None

    with open(file_path, "r") as f:
        data = json.load(f)

    return data[field]

def linear_search(seq, search):
    index = []
    for i, num in enumerate(seq):
        if num == search:
            index.append(i)

    return {"positions":index, "count": len(index)}


def main():
    unord = read_data("sequential.json", "unordered_numbers")
    print(unord)
    wanted = 0
    print(linear_search(unord, wanted))

if __name__ == '__main__':
    main()