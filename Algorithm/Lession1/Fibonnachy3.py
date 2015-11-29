import math 

def fib_mod(n, m):
    # a = 0
    # b = 1
    # c = 0
    # if n == 1:
        # c = 1
    # for i in range(1,n,1):
        # c = a + b
        # a = b
        # b = c
    c = (math.pow(((1+math.sqrt(5))/2),n) - math.pow(((1-math.sqrt(5))/2),n))/math.sqrt(5)
    return c%m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()