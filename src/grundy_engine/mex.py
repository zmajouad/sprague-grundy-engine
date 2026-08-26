def mex(numbers):
    integers = set(numbers)
    lowest = 0
    while lowest in integers:
        lowest += 1
    return lowest