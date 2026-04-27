def quick_sort(numbers: list) -> list:

    if len(numbers) < 2:
        return numbers

    pivot = numbers[0]
    less, equal, greater = [], [], []

    for num in numbers:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    return quick_sort(less) + equal + quick_sort(greater)
