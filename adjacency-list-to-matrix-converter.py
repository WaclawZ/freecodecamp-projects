def adjacency_list_to_matrix(dictionary: dict) -> list:
    dict_len = len(dictionary)
    matrix = [[0] * dict_len for _ in range(dict_len)]

    for key, value in dictionary.items():
        for el in value:
            matrix[key][el] = 1
        print(matrix[key])

    return matrix
