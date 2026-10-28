def most_frequent(numbers):
    if not numbers:
        return None

    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    most_common = None
    highest_frequency = 0

    for number in numbers:
        if frequency[number] > highest_frequency:
            highest_frequency = frequency[number]
            most_common = number

    return most_common


print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([]))
