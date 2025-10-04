def find_min_max(numbers: list) -> tuple:
    """
    Find the minimum and maximum elements in a list using
    the divide and conquer approach.
    """
    n = len(numbers)

    # Base cases
    if n == 1:
        return numbers[0], numbers[0]
    elif n == 2:
        return (
            (numbers[0], numbers[1])
            if numbers[0] < numbers[1]
            else (numbers[1], numbers[0])
        )

    # Split the list
    mid = n // 2
    left_min, left_max = find_min_max(numbers[:mid])
    right_min, right_max = find_min_max(numbers[mid:])

    # Combine results
    return (min(left_min, right_min), max(left_max, right_max))


print(find_min_max([104, 235, -5, 442, 15, 67, 71, 38, 4, 21]))
