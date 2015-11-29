#Даны целые числа 1≤n≤1018 и 2≤m≤105, необходимо найти остаток от деления n-го числа Фибоначчи на m.
def fib_mod(n, m):
    f = [0,1]
    p = 0  # Период Пизано
    for i in range(2,n):
        f.append((f[i-1]+f[i-2])%m)
        p += 1 #Подсчитываем период Пизано для данного n
        if f[i] == 1 and f[i-1] == 0:
            break
            
    #return f[int(n%p)]
    return print("P: ",p," ","n/p: ",int(n%p)," f: ",f[int(n%p)])


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()