def closest_number(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]

    for number in numbers:
        distance = abs(number - target)
        closest_distance = abs(closest - target)

        if distance < closest_distance:
            closest = number
        elif distance == closest_distance and number < closest:
            closest = number

    return closest


print(closest_number([4, 8, 15, 20], 13))
print(closest_number([8, 12], 10))
