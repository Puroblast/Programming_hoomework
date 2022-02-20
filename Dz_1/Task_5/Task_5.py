import gspread
import random
import matplotlib.pyplot as plt
sa = gspread.service_account(filename="Token.json") # Подключение сервис-аккаунта
sheet = sa.open("Task_5")  # Открытие таблицы
worksheet = sheet.worksheet("xy")   # Работа с листом

values = list(map(int,input("Введите диапазон значений через пробел: ").split()))
if len(values) == 2:
    minimum = min(values[0],values[1])
    maximum = max(values[1],values[0])
    if maximum - minimum >= 10:
        x = set()
        y = set()
        x_list = []
        y_list = []
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_xx = 0
        a = 0
        b = 0
        while len(x) < 10:
            z = random.randint(minimum,maximum)
            if z not in x:
                x_list.append(z)
                x.add(z)
        while len(y) < 10:
            z = random.randint(minimum, maximum)
            if z not in y:
                y_list.append(z)
                y.add(z)
        for i in range(len(x_list)):
            sum_xy += x_list[i]*y_list[i]
            sum_x += x_list[i]
            sum_y += y_list[i]
            sum_xx += x_list[i]**2
            worksheet.update_cell(i+1,1,x_list[i])
            worksheet.update_cell(i+1,2,y_list[i])
        a = (10*sum_xy - sum_x*sum_y)/(10*sum_xx-sum_x**2)
        b = (sum_y-a*sum_x)/10
        mnk = [[minimum,maximum],[a*minimum+b,a*maximum+b]]
        ax = plt.gca()
        ax.set_facecolor('black')
        plt.plot(mnk[0],mnk[1],c='yellow')
        plt.xlabel("Координаты X")
        plt.ylabel("Координаты Y")
        plt.title("Картина 'Ночное небо', автор Малевич К.")
        plt.scatter(x_list,y_list,c="aqua")
        plt.show()
    else:
        print("Диапазон мал")



