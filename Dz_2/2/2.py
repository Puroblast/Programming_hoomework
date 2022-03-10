import random,gspread,time,numpy as np
def returner(x1,x2,k,b):
    for x in range(x2,x1,-1):
        cell[x] = k*x + b


sa = gspread.service_account(filename="Token.json")
sheet = sa.open("random_values")
worksheet = sheet.worksheet("1")

n = int(input("Введите n: "))
worksheet.clear()
if worksheet.col_count < n:
    worksheet.add_cols(n-worksheet.col_count)
if worksheet.row_count < n:
    worksheet.add_rows(n-worksheet.col_count)
minimum = 1
maximum = 30
for i in range(n):
    for j in range(n):
        worksheet.update_cell(i+1,j+1,random.randint(minimum,maximum))
        time.sleep(1.1)

cells = worksheet.get_all_values()
cell = []
count = 0

while count != 10:
    a = random.randint(1,n)
    b = random.randint(1,n)
    if cells[a-1][b-1] != "":
        worksheet.update_cell(a,b,"")
        cells[a-1][b-1] = ""
        count += 1
        time.sleep(1.1)

for i in range(len(cells)):
    for j in cells[i]:
        cell.append(j)
def aproximation():
    flag = False
    count = 0
    for x in range(len(cell)):
        if cell[x] != "" and not flag:
            y1,x1 = int(cell[x]),x
            flag = True
            count += 1
        elif cell[x] != "" and flag:
            y2,x2 = int(cell[x]),x
            k = (y2-y1)/(x2-x1)
            b = y1 - k*x1
            returner(x1,x2,k,b)
            y1,x1 = y2,x2
            count+=1
    if count <= 1:
        print("Восстановить невозможно")
    else:
        if cell[0] == "":
            for i in range(len(cell)):
                if cell[i] != "":
                    cell[i] = float(cell[i])
                    y1, x1 = cell[i], i
                    y2,x2 = cell[x1+1], x1 + 1
                    break
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            returner(-1,x1-1,k,b)
        if cell[-1] == "":
            for i in range(len(cell)-1,-1,-1):
                if cell[i] != "":
                    cell[i] = float(cell[i])
                    y1,x1 = cell[i],i
                    y2,x2 = cell[x1-1], x1 - 1
                    break
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            returner(x1,len(cell)-1,k,b)
    for i in range(n):
        for j in range(1,n+1):
            worksheet.update_cell(i+1,j,cell[i*n+j-1])
            time.sleep(1.1)

def correlation():
    raw = int(input("ВВВ"))    #### ФУНКЦИЯ НЕДОДЕЛАНА
    corr_line = []
    for z in cells[raw]:
        corr_line.append(z)
    #corr_line = np.array(corr_line)
    coef = []
    for j in range(0,n):
        if j != raw:
            second_line_1 = []
            for z in cells[j]:
                second_line_1.append(z)
            print(n)
            print(second_line_1)
            second_line_2 = []
            for k in range(0,n):
                if corr_line[k] != "":
                    second_line_2.append(second_line_1[k])
            print(second_line_2)



aproximation()