def common_odd_even_natural(number):
    if number == 2:
        simple_numbers.append(number)
        even_numbers.append(number)
        natural_numbers.append(number)
    elif number % 2 == 0:
        even_numbers.append(number)
        if number > 0:
            natural_numbers.append(number)
    else:
        odd_numbers.append(number)
        if number > 0:
            natural_numbers.append(number)
            flag = True
            for j in range(3, int(number ** 1 / 2) + 1, 2):
                if number % j == 0:
                    flag = False
                    break
            if flag:
                simple_numbers.append(number)


def full_check(number):
    complex_numbers.append(str(complex(number)).lstrip("(").rstrip(")"))
    if str(complex(number))[-4:-1] == "+0j":
        number = str(complex(number)).split("+")[0].rstrip(")").lstrip("(")
        extended_numbers.append(number)
        ration_numbers.append(number)
        if float(number).is_integer():
            integer_numbers.append(number)
            common_odd_even_natural(int(number))


def irrational_check(number):
    splitted_number = number.split("**")
    degree_value = 1
    try:
        splitted_number = list(map(float, splitted_number))
        for i in range(len(splitted_number) - 1, 0, -1):
            degree_value = splitted_number[i] ** degree_value
        if float(degree_value).is_integer():
            full_check(str(splitted_number[0] ** degree_value))
        else:
            extended_numbers.append((splitted_number[0] ** degree_value))
            complex_numbers.append(str(complex(splitted_number[0] ** degree_value)).lstrip("(").rstrip(
                ")"))  # Приближенное значение иррационального числа
    except ValueError:
        print(f"Неверная запись числа: {number}")


def irrational_returner(number):
    splitted_number = number.split("**")
    degree_value = 1
    try:
        splitted_number = list(map(float, splitted_number))
        for i in range(len(splitted_number) - 1, 0, -1):
            degree_value = splitted_number[i] ** degree_value
        return str(splitted_number[0] ** degree_value)
    except ValueError:
        return "NoWay"


simple_numbers = []
odd_numbers = []
even_numbers = []
natural_numbers = []
integer_numbers = []
extended_numbers = []
ration_numbers = []
complex_numbers = []

numbers = input("Введите числа через запятую: ").replace(" ", "").split(",")
for i in numbers:
    try:
        full_check(i)
    except ValueError:
        if i[-1] == "j":
            i = i.split("+")
            if len(i) == 2:
                a = irrational_returner(i[0])
                b = irrational_returner(i[1][:-1])
                if a == "NoWay" or b == "NoWay":
                    print(f"Неверная запись числа")
                else:
                    if b == "0.0":
                        full_check(a)
                    else:
                        complex_numbers.append(f"{a}+{b}j")
            elif len(i) == 1:
                b = irrational_returner(i[0][:-1])
                if b == "NoWay":
                    print(f"Неверная запись числа")
                else:
                    complex_numbers.append(f"{b}j")

            else:
                print(f"Неверная запись числа")
        else:
            irrational_check(i)

print(f"Простые числа : {' '.join(map(str, simple_numbers))}\n"
      f"Нечетные числа : {' '.join(map(str, odd_numbers))}\n"
      f"Четные числа : {' '.join(map(str, even_numbers))}\n"
      f"Натуральные числа : {' '.join(map(str, natural_numbers))}\n"
      f"Целые числа : {' '.join(map(str, integer_numbers))}\n"
      f"Рациональные числа : {' '.join(map(str, ration_numbers))}\n"
      f"Вещественные числа : {' '.join(map(str, extended_numbers))}\n"
      f"Комплексные числа : {' '.join(map(str, complex_numbers))}")
