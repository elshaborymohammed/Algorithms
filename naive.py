# counting steps in naive as a function of a
import math
import time

def multiply(a,b):
    x = a
    y = b
    z = 0
    start = time.time();
    while x > 0:
        z = z + y
        x = x - 1
    end = time.time();
    print "{} = {}".format("time taken", (end - start))
    return z

def steps(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 3 + 2 * math.ceil(a);
    # your code here
    return steps
