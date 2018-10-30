def factorial(n):
    '''
    This program calculates the factorial of any number recursively
    :param n: Number inputted by the user
    :precondition: The number cannot be negative
    :postcondition: The factorial of the number is calculated
    :return: The factorial of the number
    :complexity: Best Case = Worst Case = O(2^n), where n is the number input by the user
    '''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
