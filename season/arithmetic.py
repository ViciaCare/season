a = int(input("Введите число "))
b = int(input("Введите число "))
operation = str(input("Введите операцию "))


def arithmetic():
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    print(result)


arithmetic()
