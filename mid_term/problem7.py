def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    for number in range(0, 101):
        if test(number) is True:
            return number

    for number in range(-100, 0):
        if test(number) is True:
            return number
    
    # IMPLEMENT THIS FUNCTION


# #### This test case prints 49 ####
# def f(x):
#     return (x+15)**0.5 + x**0.5 == 15

#### This test case prints 0 ####
def f(x):
    return x == 0
# print(solveit(f))

if __name__ == '__main__':
    print(solveit(f))
