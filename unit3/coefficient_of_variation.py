import math


def coefficientOfVariation(L):
    """Returns the coefficient of variation to 3 decimal places
    Assumes L is a list of integers
    """

    # Get the mean of the length of the words
    count = 0
    for number in L:
        count += number
    mean = count / len(L)

    # Compute the standard deviation using the mean
    numerator = 0
    for number in L:
        std_dev = (number - mean) ** 2
        numerator += std_dev

    std_dev = math.sqrt((numerator / len(L)))
    
    coefficient_of_variation = std_dev / mean

    return round(coefficient_of_variation, 3)


if __name__ == '__main__':
    print(coefficientOfVariation([10, 4, 12, 15, 20, 5]))