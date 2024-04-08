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

def main():
    #pass
    sequentationl_data = read_data("sequential.json", "unordered_numbers")
    print(sequentationl_data)

if __name__ == '__main__':
    main()