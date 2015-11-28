#Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2 при n≥2).

def fib(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        c = 1
    for i in range(1,n,1):
        c = a + b
        a = b
        b = c
    return c

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()