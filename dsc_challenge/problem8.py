def insertion_sort(numbers):
    shifts = 0

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            shifts += 1
            j -= 1

        numbers[j + 1] = key

    return numbers, shifts

print(insertion_sort([5, 3, 4]))
print(insertion_sort([1, 2, 3]))
