import random, gspread, time


def aproximation():
    flag = False
    count = 0
    for x in range(len(cell)):
        if cell[x] != "" and not flag:
            y1, x1 = int(cell[x]), x
            flag = True
            count += 1
        elif cell[x] != "" and flag:
            y2, x2 = int(cell[x]), x
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            returner(x1, x2, k, b)
            y1, x1 = y2, x2
            count += 1
    if count <= 1:
        print("Восстановить невозможно")
    else:
        if cell[0] == "":
            for i in range(len(cell)):
                if cell[i] != "":
                    cell[i] = float(cell[i])
                    y1, x1 = cell[i], i
                    y2, x2 = cell[x1 + 1], x1 + 1
                    break
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            returner(-1, x1 - 1, k, b)
        if cell[-1] == "":
            for i in range(len(cell) - 1, -1, -1):
                if cell[i] != "":
                    cell[i] = float(cell[i])
                    y1, x1 = cell[i], i
                    y2, x2 = cell[x1 - 1], x1 - 1
                    break
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            returner(x1, len(cell) - 1, k, b)
    for i in range(n):
        for j in range(1, n + 1):
            worksheet.update_cell(i + 1, j, cell[i * n + j - 1])
            time.sleep(1.1)


def returner(x1, x2, k, b):
    for x in range(x2, x1, -1):
        cell[x] = k * x + b


def regcoef(array1, array2):
    middlex = 0
    middley = 0
    fluctsumxy = 0
    fluctsumx = 0
    fluctsumy = 0
    for i in array1:
        middlex += i
    for i in array2:
        middley += i
    middlex = middlex / len(array1)
    middley = middley / len(array2)
    for i in range(len(array1)):
        fluctsumxy += (array1[i] - middlex) * (array2[i] - middley)
        fluctsumx += (array1[i] - middlex) ** 2
        fluctsumy += (array2[i] - middley) ** 2
    rxy = fluctsumxy / ((fluctsumx * fluctsumy) ** (1 / 2))
    return rxy


def little_squares(array1, array2):
    sumxy = 0
    sumx = 0
    sumy = 0
    sumx2 = 0
    for i in range(len(array1)):
        sumxy += array1[i] * array2[i]
        sumx += array1[i]
        sumy += array2[i]
        sumx2 += array1[i] ** 2
    a = (len(array1) * sumxy - sumx * sumy) / (len(array1) * sumx2 - (sumx) ** 2)
    b = (sumy - a * sumx) / len(array1)
    return a, b


def correlation():
    raw = int(input("Введите коррелируемую строку: ")) - 1
    corr_line = []
    coeffs = {}
    lines = {}
    for i in cells[raw]:
        corr_line.append(i)
    for i in range(len(cells)):
        if i != raw:
            corr_line_up = []
            line = []
            flag = True
            for j in range(len(cells[i])):
                if corr_line[j] == "" and cells[i][j] == "":
                    flag = False
                    break
                if corr_line[j] != "" and cells[i][j] != "":
                    corr_line_up.append(int(corr_line[j]))
                    line.append(int(cells[i][j]))
            if flag:
                if len(corr_line_up) > 2:
                    coeffs[i] = regcoef(corr_line_up, line)
                    lines[i] = [line, corr_line_up]
    max = 0
    maxindex = 0
    for key in coeffs:
        if abs(coeffs[key]) > max:
            max = coeffs[key]
            maxindex = key
    if len(lines) > 0:
        a, b = little_squares(lines[maxindex][0], lines[maxindex][1])
        for i in range(len(corr_line)):
            if corr_line[i] == "":
                x = int(cells[maxindex][i])
                corr_line[i] = a * x + b
    else:
        print("Невозможно посчитать")
    return corr_line, raw


sa = gspread.service_account(filename="Token.json")
sheet = sa.open("random_values")
worksheet = sheet.worksheet("1")

n = int(input("Введите n: "))
worksheet.clear()
if worksheet.col_count < n:
    worksheet.add_cols(n - worksheet.col_count)
if worksheet.row_count < n:
    worksheet.add_rows(n - worksheet.col_count)
minimum = 1
maximum = 30
for i in range(n):
    for j in range(n):
        worksheet.update_cell(i + 1, j + 1, random.randint(minimum, maximum))
        time.sleep(1.1)

cells = worksheet.get_all_values()
cell = []
count = 0

while count != 10:
    a = random.randint(1, n)
    b = random.randint(1, n)
    if cells[a - 1][b - 1] != "":
        worksheet.update_cell(a, b, "")
        cells[a - 1][b - 1] = ""
        count += 1
        time.sleep(1.1)

for i in range(len(cells)):
    for j in cells[i]:
        cell.append(j)

line, raw = correlation()
for i in range(len(line)):
    worksheet.update_cell(raw + 1, i + 1, line[i])
    time.sleep(1.1)
