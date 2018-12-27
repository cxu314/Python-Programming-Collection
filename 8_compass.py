def minimumDistance(n1, n2):
    """
    This function takes an integer n1, the current direction of the needle,
    and an integer n2, the correct direction of the needle.

    This function returns the change in direction that would make the needle
    spin the shortest distance from n1 to n2.
    A positive change indicates spinning the needle clockwise,
    and a negative change indicates spinning the needle counter-clockwise.
    If the two input numbers are diametrically opposed,
    the needle should travel clockwise.
    """
    if n2 >= n1:
        x1 = n2 - n1
    else:
        x1 = n2 + 360 - n1

    if n1 >= n2:
        x2 = n2 - n1
    else:
        x2 = n2 - (n1 + 360)

    if abs(x1) <= abs(x2):
        return x1
    else:
        return x2


if __name__ == "__main__":
    import sys

    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    print(minimumDistance(n1, n2))
