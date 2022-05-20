from openpyxl import Workbook
from math import sin,pi,log,e,cos
import matplotlib.pyplot as plt


def smooth(end_index,delta):
    global float_index
    while float_index <= end_index:
        kx = 0
        for j in range(end_index, float_index - 1,-1):
            kx += numbers[j]
        x = kx / (end_index - float_index + 1)
        if abs(numbers[end_index] - x) / numbers[end_index] > int(delta) / 100:
            float_index += 1
            continue
        else:
            smooth_numbers.append(x)
            break

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


wb = Workbook()

numbers = []
smooth_numbers = []
MNK_smooth = []
MNK = []

float_index = 0

ws = wb.active
start,end,step = map(float,input("Введите начальное значение,конечное значение и шаг через пробел : ").split())
start1 = start
start2 = start1
x_values = []

while start <= end:
    f = sin(start) + 0.1 * sin(start**5)
    ws.append([f])
    x_values.append(start)
    start += step

#while start <= end:
    #f = sin(pi*sin(start)) + log(start,e)
    #ws.append([f])
    #x_values.append(start)
    #start += step

#while start <= end:
    #f = start * cos(10*start) + start**2 + start
    #ws.append([f])
    #x_values.append(start)
    #start += step

for i in ws.values:
    for cell in i:
        numbers.append(cell)

wb.save("sample.xlsx")

for i in range(len(numbers)):
    smooth(i,25)

a,b = little_squares(x_values,smooth_numbers)

while start1 <= end:
    f = a * start1 + b
    MNK_smooth.append(f)
    start1 += step

a,b = little_squares(x_values,numbers)

while start2 <= end:
    f = a * start2 + b
    MNK.append(f)
    start2 += step

next_number = (2 * numbers[-1] - numbers[-2])
next_smooth_number = (2 * smooth_numbers[-1] - smooth_numbers[-2])
delta = abs(next_number - next_smooth_number) / next_number

print(numbers)
print(next_number)
print()
print(smooth_numbers)
print(next_smooth_number)

fig = plt.plot(smooth_numbers,label="Numbers smooth")
plt.plot(MNK,label= "MNK")
plt.plot(numbers,label="common numbers")
plt.plot(MNK_smooth,label="MNK SMOOTH")

plt.legend(fontsize=16.5,
           ncol=1,
           edgecolor='b',
           title='Кривые',
           title_fontsize='15')

plt.show()