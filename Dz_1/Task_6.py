def matrix(i):
    while True:
        try:
            line = list(map(int, input(f"Введите {i + 1} строку через пробел: ").split()))
            break
        except ValueError:
            print("Неверный ввод")
    if len(line) == columns:
        return line
    else:
        print("Неверно введены данные")
        return matrix(i)


def transpon(array):
    transpon_array = []
    for i in range(columns):
        line = []
        for j in range(lines):
            line.append(0)
        transpon_array.append(line)
    for i in range(len(array)):
        for j in range(len(array[i])):
            transpon_array[j][i] = array[i][j]
    print("Транспонированная матрица :")
    for i in range(len(transpon_array)):
        for j in range(len(transpon_array[i])):
            print(transpon_array[i][j], end=" ")
        print()


def square(array):
    if lines == columns:
        square_array = []
        for i in range(len(array)):
            line = []
            for j in range(len(array[i])):
                line.append(0)
            square_array.append(line)
        for i in range(len(array)):  # строка
            for j in range(len(array[i])):  # столбец
                for z in range(len(array)):  # номер числа внутри строки и столбца
                    square_array[i][j] += array[i][z] * array[z][j]
        print("Квадрат матрицы :")
        for i in range(len(square_array)):
            for j in range(len(square_array[i])):
                print(square_array[i][j], end=" ")
            print()
    else:
        print("Количество строк не совпадает с количеством столбцов")


def det(array):
    if lines == columns:
        if len(array) == 2:
            return array[0][0] * array[1][1] - array[0][1] * array[1][0]
        else:
            sum = 0
            for i in range(len(array)):
                new_array = []
                for j in range(1, len(array)):
                    line = []
                    for k in range(len(array[j])):
                        if k != i:
                            line.append(array[j][k])
                    new_array.append(line)
                sum += array[0][i] * (-1) ** ((i + 1) + (0 + 1)) * det(new_array)
        return sum
    else:
        print("Определитель найти невозможно")


while True:
    try:
        lines = int(input("Введите количество строк матрицы: "))
        break
    except ValueError:
        print("Неверный ввод")
while True:
    try:
        columns = int(input("Введите количество столбцов матрицы: "))
        break
    except ValueError:
        print("Неверный ввод")
lines_array = []
for k in range(lines):
    lines_array.append(matrix(k))
print("Ваша матрица:")
for i in range(len(lines_array)):
    for j in range(len(lines_array[i])):
        print(lines_array[i][j], end=" ")
    print()
commands = ["transpon", "square", "det", "exit"]

while True:
    command = input(f"Введите команду, доступные команды: {', '.join(commands)} : ")
    if command == commands[0]:
        transpon(lines_array)
    elif command == commands[1]:
        square(lines_array)
    elif command == commands[2]:
        if det(lines_array) is not None:
            print(f"Определитель матрицы :\n {det(lines_array)}")
    elif command == commands[3]:
        break
    else:
        print("Неизвестная команда")
