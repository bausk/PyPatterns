import math

def identity(x):
    """
    :type f1: object
    :type f2: object
    :rtype: object
    """
    return x

a = identity("11")

def plusone(x):
    return x+1

def comp(f1, f2):
    """
    :type f1: function
    :type f2: function
    :rtype: function
    """
    def f3(x):
        x = f1(f2(x))
        return x
    return f3

a = comp(identity, identity)

print a
print a(1)
