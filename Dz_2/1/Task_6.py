def transpon(array, lines, columns):
    transpon_array = []
    for i in range(columns):
        line = []
        for j in range(lines):
            line.append(0)
        transpon_array.append(line)
    for i in range(len(array)):
        for j in range(len(array[i])):
            transpon_array[j][i] = array[i][j]
    return transpon_array


def square(array, lines, columns):
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
        return square_array
    else:
        print("Количество строк не совпадает с количеством столбцов")


def det(array, lines, columns):
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
                sum += array[0][i] * (-1) ** ((i + 1) + (0 + 1)) * det(new_array, lines - 1, columns - 1)
        return sum
    else:
        print("Определитель найти невозможно")
