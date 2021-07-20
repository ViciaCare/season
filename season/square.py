def square(a):
    return (a * 4, a ** 2, (2 * a ** 2) ** .5)


result = square(int(input("Введите сторону квадрата ")))
print(result)
