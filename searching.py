import os
import json

def read_data(file_name, field):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as f:
        allowed_key = json.load(f)
        if field not in allowed_key:
            return None
    with open(file_name, "r") as f:
        data = json.load(f)

    return data.get(field)

def linear_search(sekvence, number):

    position = []
    count = 0
    for i, num in enumerate(sekvence):
        if num == number:
            position.append(i)
            count = count + 1
    slovnik = {"Possitions":position,"count":count}
    return slovnik

def pattern_search(my_sequence, vzor):
    delka = len(vzor)
    position = set()
    for i in range(len(my_sequence)-delka):
        prvek = my_sequence[i:delka + i]
        if prvek == vzor:
            position.add(i)

#def binary_search(my_numbers, number):





def main():
    #pass
    sequentationl_data = read_data("sequential.json", "unordered_numbers")
    sequentationl_data1 = read_data("sequential.json","dna_sequence")
    sequentationl_data2 = read_data("sequential.json",  "ordered_numbers")
    print(sequentationl_data)
    linear = linear_search(sequentationl_data, 1)
    print(linear)
    porovnani = pattern_search(sequentationl_data1, "ATA")
    print(porovnani)
    #binary = pattern_search(sequentationl_data2,3)
    #print(binary)

if __name__ == '__main__':
    main()