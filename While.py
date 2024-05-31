#9.
#a.
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = int(input("Введіть кількість чисел Фібоначчі: "))
fib_series = fibonacci(n)
print("#a Ряд чисел Фібоначчі:", fib_series)

#b.
def fibonacci_range(start, end):
    fib_series = []
    a, b = 0, 1
    count = 0
    while count < end:
        if count >= start:
            fib_series.append(a)
        a, b = b, a + b
        count += 1
    return fib_series

fib_series = fibonacci_range(5, 21)
print("#b Ряд чисел Фібоначчі з 5-го по 20-й", fib_series)
