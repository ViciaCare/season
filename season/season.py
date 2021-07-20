i=int(input("Введите месяц цифрой от 1 до 12 " ))


def season():
    if i<=3:
        print("зима")
    elif i>3 and i<=6:
        print("весна")
    elif i>6 and i<=9:
        print("лето")
    else:
        print("осень")


season()

