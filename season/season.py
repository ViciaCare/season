i=int(input("Введите месяц цифрой от 1 до 12 " ))


def season():
    if i<=2 or i==12:
        print("зима")
    elif i>=3 or i<=5:
        print("весна")
    elif i>5 or i<=8:
        print("лето")
    else:
        print("осень")


season()

