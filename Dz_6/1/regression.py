import gspread
import math
import matplotlib.pyplot as plt
import random


def cov(X, Y):
    average_x = sum(X) / len(X)
    average_y = sum(Y) / len(Y)
    numenator = 0
    for i in range(len(X)):
        numenator += (Y[i] - average_y) * (X[i] - average_x)

    return numenator / (len(X) - 1)


def var(X):
    average_x = sum(X) / len(X)
    numenator = 0
    for i in range(len(X)):
        numenator += math.pow((X[i] - average_x), 2)

    return numenator / len(X)


def findB(X, Y):
    numerator = cov(X, Y)
    denominator = var(X)
    return numerator / denominator


def findA(X, Y,b):
    a = 0
    for i in range(len(X)):
        a += Y[i] - b * X[i]
    return a / len(X)

def regression(data):
    X = data[:-1]
    Y = data[1:]
    b = findB(X, Y)
    a = findA(X, Y,b)
    print(a,b)
    result = []

    for i in data:
        result.append(a + b * i + random.uniform(-0.01 * i, 0.01 * i))

    fig, ax = plt.subplots()
    ax.plot(data)
    ax.plot(result)
    plt.show()

gc = gspread.service_account(filename="Token.json")
gsheet = gc.open("MySheet").worksheet("1")
data_all = gsheet.get_all_records()
series = []
for i in range(len(data_all)):
    series.append(data_all[i].get('price'))
regression(series)
