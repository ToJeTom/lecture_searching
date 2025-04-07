import os, json
from ast import literal_eval
from operator import index

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
    index = [] #+1
    for i, num in enumerate(seq): #+n
        if num == search: #+1*n
            index.append(i) #+x

    return {"positions":index, "count": len(index)} #+1

def pattern_search(seq, patt):
    idx = set()
    for i in range(len(seq) - 4):
        if seq[i:i + 3] == patt:
            idx.add(i)

    return idx

def binary_search(seq, search):
    mid = len(seq) // 2
    right = len(seq) - 1
    left = 0
    if seq[right] == search:
        return right
    if seq[left] == search:
        return left

    while True:
        if seq[mid] == search:
            return mid
        elif seq[mid] < search:
            left = mid
        else:
            right = mid
        mid = (right + left) // 2
        if left + 1 == right:
            return None





def main():
    unord = read_data("sequential.json", "unordered_numbers")
    #print(unord)

    wanted = 0
    #print(linear_search(unord, wanted))

    sequence = read_data("sequential.json","dna_sequence")
    #print(pattern_search(sequence, "ATA"))

    ordered = read_data("sequential.json", "ordered_numbers")
    searNm = 102
    print(binary_search(ordered, searNm))


if __name__ == '__main__':
    main()