def count_even(numbers):
    if not numbers:
        return 0
    
    even = 0

    for number in numbers:
        if number % 2 == 0:
            even = even + 1

    return even

print(count_even([1, 2, 3, 4, 6]))
print(count_even([1, 3, 5, 7]))

