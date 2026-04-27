def selection_sort(numbers: list) -> list:
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        if min_index != i:
            numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers
