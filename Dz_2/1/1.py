from Task_6 import *
from Shtrassen import *
import time, numpy as np, matplotlib.pyplot as plt, random as rnd

matrix_size = []
our_time_square = []
np_time_square = []
our_new_time_sq = []
our_time_trans = []
np_time_trans = []
our_time_det = []
np_time_det = []


def our_code(func, array):
    start_time = time.perf_counter()
    func(array, i, i)
    end_time = time.perf_counter()
    return end_time - start_time


def our_new_code(func, array):
    start_time = time.perf_counter()
    delete_zeros(func(array, array))
    end_time = time.perf_counter()
    return end_time - start_time


def np_code(func, array, degree=None):
    new_array = []
    for _ in array:
        line = []
        for l in _:
            line.append(l)
        new_array.append(line)
    if degree is not None:
        start_time = time.perf_counter()
        func(new_array, degree)
        end_time = time.perf_counter()
    else:
        start_time = time.perf_counter()
        func(new_array)
        end_time = time.perf_counter()
    return end_time - start_time


for i in range(2, 5):
    matrix = []
    matrix_size.append(i)
    for j in range(i):
        line = []
        for k in range(i):
            line.append(rnd.randint(1, 5))
        matrix.append(line)
    our_time_square.append(our_code(square, matrix))
    our_time_det.append(our_code(det, matrix))
    our_time_trans.append(our_code(transpon, matrix))
    our_new_time_sq.append(our_new_code(strassen, matrix))
    np_time_square.append(np_code(np.linalg.matrix_power, matrix, 2))
    np_time_det.append(np_code(np.linalg.det, matrix))
    np_time_trans.append(np_code(np.transpose, matrix))

fig, axs = plt.subplots(1, 3)
axs[0].set_title("Возведение в квадрат")
axs[0].set_xlabel("Размер матрицы")
axs[0].set_ylabel("Время выполнения")
axs[0].plot(matrix_size, np_time_square, label="Функция из NumPy")
axs[0].plot(matrix_size, our_time_square, label="Функция из Task_6")
axs[0].plot(matrix_size, our_new_time_sq, label="Штрассен")

axs[1].set_title("Нахождение определителя")
axs[1].set_xlabel("Размер матрицы")
axs[1].set_ylabel("Время выполнения")
axs[1].plot(matrix_size, np_time_det)
axs[1].plot(matrix_size, our_time_det)
axs[2].set_title("Транспонирование")
axs[2].set_xlabel("Размер матрицы")
axs[2].set_ylabel("Время выполнения")
axs[2].plot(matrix_size, np_time_trans)
axs[2].plot(matrix_size, our_time_trans)

fig.legend(fontsize=16.5,
           ncol=1,
           edgecolor='b',
           title='Прямые',
           title_fontsize='15')
plt.show()
