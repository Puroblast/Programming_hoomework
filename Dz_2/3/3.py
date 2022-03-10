import random,gspread,time

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


normal_math_waiting = ((minimum + maximum) * (maximum / 2)) / maximum
normal_dispers = 0
cells = worksheet.get_all_values()
for i in range(minimum,maximum+1):
    normal_dispers += normal_dispers + (normal_math_waiting - i)**2
normal_dispers = normal_dispers / maximum
for i in range(n):
    dispers = 0
    summa = sum(map(int,cells[i])) / n
    for j in range(n):
        dispers = dispers + (int(cells[i][j]) - summa)**2
    dispers = dispers / n
    print(f"Математическое ожидание {i+1} строки: {summa}")
    print(f"Дисперсия для {i+1} строки: {dispers}")

print(f"Ожидаемое математическое ожидание: {normal_math_waiting}")
print(f"Ожидаемая дисперсия: {normal_dispers}")

