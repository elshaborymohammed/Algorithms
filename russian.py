import time
def multiply(a,b):
    x = a; y = b; z = 0;
    start = time.time();
    while x > 0:
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    end = time.time();
    print "time taken = ", (end - start)
    return z
