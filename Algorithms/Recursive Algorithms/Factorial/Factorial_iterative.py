def factorial(n):
    '''
    This program calculates the factorial of any number iteratively
    :param n: Number inputted by the user
    :precondition: The number cannot be negative
    :postcondition: The factorial of the number is calculated
    :return: The factorial of the number
    :complexity: Best Case = Worst Case = O(n), where n is the number of times the loop will run
    '''

    assert n >= 0, 'The number cannot be negative'
    product = 1
    i = 0
    while i < n:
        product = product * (i + 1)
        i += 1
    return product
