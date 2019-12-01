import math

def stdDevOfLengths(L=None):
    """Return the standard deviation on the length of strings.  
    Expects L to be a list. 
        Returns standard deviation
        Returns 'NaN' if the list is empty
    """
    if not L or len(L) < 1:
        return float('NaN')
    
    # Get the mean of the length of the words
    count = 0
    for word in L:
        count += len(word)
    mean = count / len(L)

    # Compute the standard deviation using the mean
    numerator = 0
    for word in L:
        std_dev = (len(word) - mean) ** 2
        numerator += std_dev

    std_dev = math.sqrt((numerator / len(L)))

    return std_dev
        
if __name__ == '__main__':
    # Basic tests
    L1 = ['a', 'z', 'p']
    L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
    print(stdDevOfLengths(L1))
    print(stdDevOfLengths(L2))