def test():
    pass


def fibonacci(n):
    """
    a simple recursive sequence to
    produce the fibonacci sequence
    for a desired number.
    :param n:
    :return desired number sequence num:
    """

    # old unused code
    # if n == 1:
    #     return 1
    #
    # return n + fibonacci(n + 1)

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    a simple recursive sequence to
    produce the lucas sequence
    for a desired number.
    :param n:
    :return desired number sequence num:
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """
    a function to take in a value and
    two optional values specifying the
    first incrimented numbers. If no
    optional input is done, default
    to the fibonacci sequence.

    :param n:
    :param a:
    :param b:
    :return desired number sequence, with optional
    user input values for a and b:
    """
    # sequence = [a, b]
    # while len(sequence) < n:
    #     sequence.append(sequence[-1] + sequence[-2])
    # return sequence
    # print(sum_series())

    if n <= 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
