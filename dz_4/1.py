from tkinter import *
from tkinter.ttk import *
import requests
import matplotlib.pyplot as plt

def bb(status):
    def build(id,oldDay,oldMonth,oldYear,newDay,newMonth,newYear,recovery,smooth,delta):
        kekdata = []
        good_data = []
        if int(oldMonth) / 10 < 1:
            oldMonth = "0"+oldMonth
        if int(oldDay) / 10 < 1:
            oldDay = "0"+oldDay
        if int(newDay) / 10 < 1:
            newDay = "0" + newDay
        if int(newMonth) / 10 < 1:
            newMonth = "0"+newMonth
        req = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{id}.json?from={oldYear}-{oldMonth}-{oldDay}&till={newYear}-{newMonth}-{newDay}&history.columns=TRADEDATE,OPEN&iss.meta=off"
        bigdata = requests.get(req).json()["history"]["data"]
        lol = 31 * (12 * (int(newYear)-int(oldYear)) + int(newMonth) - int(oldMonth))
        if lol >= 100 :
            lol = 100 // 31
        allData = [[0 for _ in range(31)] for i in range(lol // 31 + 1)]
        k = 0
        for i in range(len(allData)):
            for j in range(len(allData[i])):
                if k == len(bigdata):
                    break
                print(k)
                strin = bigdata[k][0]
                if j + 1 == int(strin[len(strin) - 2:]) :
                    allData[i][j] = bigdata[k][1]
                    k += 1

        for i in range(len(allData)):
            for j in range(len(allData[i])):
                if i == int(newMonth) - int(oldMonth) and j == int(newDay):
                    break
                elif i == 0 and j + 1 == int(oldDay):
                    good_data.append(allData[i][j])
                else:
                    good_data.append(allData[i][j])
        print(good_data)
        print(allData)
        if recovery == "Винзорирование":
            for i in range(len(good_data) - 1):
                if good_data[i+1] == 0 and good_data[i] != 0:
                    good_data[i+1] = good_data[i]
            if good_data[0] == 0:
                for i in range(1,len(good_data)):
                    if good_data[i] != 0 :
                        for j in range(i - 1, -1,-1):
                            good_data[j] = good_data[i]
                        break
        elif recovery == "Линейная аппроксимация":
            def returner(x1, x2, k, b):
                for x in range(x2, x1, -1):
                    good_data[x] = k * x + b
            flag = False
            count = 0
            for x in range(len(good_data)):
                if good_data[x] != 0 and not flag:
                    y1, x1 = int(good_data[x]), x
                    flag = True
                    count += 1
                elif good_data[x] != 0 and flag:
                    y2, x2 = int(good_data[x]), x
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                    returner(x1, x2, k, b)
                    y1, x1 = y2, x2
                    count += 1
            if count <= 1:
                print("Восстановить невозможно")
            else:
                if good_data[0] == 0:
                    for i in range(len(good_data)):
                        if good_data[i] != 0:
                            good_data[i] = float(good_data[i])
                            y1, x1 = good_data[i], i
                            y2, x2 = good_data[x1 + 1], x1 + 1
                            break
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                    returner(-1, x1 - 1, k, b)
                if good_data[-1] == 0:
                    for i in range(len(good_data) - 1, -1, -1):
                        if good_data[i] != 0:
                            good_data[i] = float(good_data[i])
                            y1, x1 = good_data[i], i
                            y2, x2 = good_data[x1 - 1], x1 - 1
                            break
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                    returner(x1, len(good_data) - 1, k, b)

        if smooth == "Взвешенный метод скользящего среднего":
            kekdata = [0] * len(good_data)
            summ = 0
            for t in range(0, len(good_data)):
                summ = summ + good_data[t] * (t + 1)
                kekdata[t] = 2 / ((t + 1) * (t + 2)) * summ
        else:

            def moveAverage(step, i):
                xk = 0
                n = 0
                for j in range(i, i - step - 1, -1):
                    if j >= 0:
                        xk += good_data[j]
                        n += 1
                    else:
                        break
                x = xk / n
                if abs(good_data[i] - x) / good_data[i] > int(delta)/100:
                    moveAverage(step - 1, i)
                else:
                    kekdata.append(x)
            for i in range(len(good_data)):
                moveAverage(len(good_data) - 1, i)
        print(kekdata)
        print(good_data)
        fig = plt.plot([i for i in range(len(kekdata))], kekdata, label="Сглаженный")
        plt.plot([i for i in range(len(kekdata))], good_data, label="До сглаживания")
        plt.legend(fontsize=16.5,
                   ncol=1,
                   edgecolor='b',
                   title='Кривые',
                   title_fontsize='15')
        plt.show()

    def buildButtonPressed():
        nonlocal status
        if status == 1:
            print(status)
            id = tickerBox.get()
            oldDay = oldDayBox.get()
            oldMonth = oldMonthBox.get()
            oldYear = oldYearBox.get()
            newDay = newDayBox.get()
            newMonth = newMonthBox.get()
            newYear = newYearBox.get()
            recovery = recoveryChoiceBox.get()
            smooth = smoothChoiceBox.get()
            delta = deltaBox.get()
            print(id,oldDay,oldMonth,oldYear,newDay,newMonth,newYear,recovery,smooth,delta)
            if id == "" or oldDay  == "" or oldMonth == "" or oldYear == "" or newDay  == "" or newMonth == "" or newYear == "" or recovery  == "" or smooth == "" or delta == "" :
                pass
            else :
                status = (status + 1) % 2
                build(id,oldDay,oldMonth,oldYear,newDay,newMonth,newYear,recovery,smooth,delta)
        else:
            print("Кнопка уже нажата")
    return buildButtonPressed
root = Tk()

height = 500
width = 500
root.geometry(f"{height}x{width}")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

ID = ["GAZP", "TATN", "SBER", "VTBR", "ALRS",
      "AFLT", "HYDR", "MOEX", "NLMK", "CHMF",
      "DSKY", "RUSP", "YNDX", "AFKS", "LSRG",
      "LSNG", "LKOH", "MTSS", "NVTK", "PIKK"]

days = [str(i) for i in range(1,32)]
months = [str(i) for i in range(1,13)]
years = [str(i) for i in range(2015,2023)]
recoveryChoices = ["Винзорирование","Линейная аппроксимация"]
smoothChoices = ["Взвешенный метод скользящего среднего","Мето скользящего среднего со скользящим окном"]

tickerLabel = Label(text="Выберите компанию: ")
tickerLabel.place(x=0,y=0,width=width//4)

tickerBox = Combobox(root, values=ID)
tickerBox["state"] = "readonly"
tickerBox.place(x=width//4,y=0,width=int(width * 0.75))

fromLabel = Label(text="Выберите начало периода.")
fromLabel.place(x=width//2.78,y=height // 16,width=width // 2)

oldDayLabel = Label(text="День:")
oldDayLabel.place(x=0,y=height // 10 , width=width // 12)
oldDayBox = Combobox(root,values=days)
oldDayBox["state"] = "readonly"
oldDayBox.place(x=width//12,y=height // 10,width=width // 5)

oldMonthLabel = Label(text="Месяц:")
oldMonthLabel.place(x=width * 4 // 12,y=height // 10 , width=width // 12)
oldMonthBox = Combobox(root,values=months)
oldMonthBox["state"] = "readonly"
oldMonthBox.place(x=width * 5//11,y=height // 10,width=width // 5)

oldYearLabel = Label(text="Год:")
oldYearLabel.place(x=width * 3 // 4.1,y=height // 10 , width=width // 12)
oldYearBox = Combobox(root,values=years)
oldYearBox["state"] = "readonly"
oldYearBox.place(x=width * 4 // 5,y=height // 10,width=width // 5)

toLabel = Label(text="Выберите конец периода.")
toLabel.place(x=width//2.78,y=height // 6.5,width=width // 2)

newDayLabel = Label(text="День:")
newDayLabel.place(x=0,y=height // 5 , width=width // 12)
newDayBox = Combobox(root,values=days)
newDayBox["state"] = "readonly"
newDayBox.place(x=width//12,y=height // 5,width=width // 5)

newMonthLabel = Label(text="Месяц:")
newMonthLabel.place(x=width * 4 // 12,y=height // 5 , width=width // 12)
newMonthBox = Combobox(root,values=months)
newMonthBox["state"] = "readonly"
newMonthBox.place(x=width * 5//11,y=height // 5,width=width // 5)

newYearLabel = Label(text="Год:")
newYearLabel.place(x=width * 3 // 4.1,y=height // 5 , width=width // 12)
newYearBox = Combobox(root,values=years)
newYearBox["state"] = "readonly"
newYearBox.place(x=width * 4 // 5,y=height // 5,width=width // 5)

recoveryChoiceLabel = Label(text="Выберите способ восстановления: ")
recoveryChoiceLabel.place(x=0,y=height // 3,width=width//2)
recoveryChoiceBox = Combobox(root,values=recoveryChoices)
recoveryChoiceBox["state"] = "readonly"
recoveryChoiceBox.place(x=width//2, y=height // 3, width=width//2)

smoothChoiceLabel = Label(text="Выберите метод сглаживания: ")
smoothChoiceLabel.place(x=0,y=height // 2,width=width//2.5)
smoothChoiceBox = Combobox(root,values=smoothChoices)
smoothChoiceBox["state"] = "readonly"
smoothChoiceBox.place(x=width//2.5, y=height // 2, width=width//1.66)

deltaLabel = Label(text="Выберите максимальное отклонение в %: ")
deltaLabel.place(x=0, y=height// 1.5)
deltaBox = Entry(root)
deltaBox.place(x= width // 2, y = height // 1.5,width=width//2)
function = bb(1)
buildButton = Button(text = "BUILD",command=function)
buildButton.place(x = width // 2.2,y=height// 1.2)

root.mainloop()



