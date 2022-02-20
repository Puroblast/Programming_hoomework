def check(name):
    while True:
        try:
            n = float(input(f"Введите число от 0 до 1 - Вероятность происхождения события с {name} за {c} дней: "))
            if 1 >= n >= 0:
                return n
            else:
                print("Неверные данные")
        except ValueError:
            print("Неверные данные")
            return check(name)


def lucky_man():
    not_prob_one_day_andrey = (1 - n_a) ** (1 / c)  # Вероятность того что с Андреем ничего не произойдет за 1 день
    prob_d_day = 1 - not_prob_one_day_andrey ** d  # Вероятность того что с Андреем произойдет событие за D дней

    not_prob_one_day_masha = (1 - n_m) ** (1 / c)
    not_prob_d_day_masha = not_prob_one_day_masha ** d  # Вероятность того что с Машей ничего не произойдет за D дней

    not_prob_one_day_tanya = (1 - n_t) ** (1 / c)
    not_prob_d_day_tanya = not_prob_one_day_tanya ** d  # Вероятность того что с Таней ничего не произойдет за D дней
    return prob_d_day * not_prob_d_day_tanya * not_prob_d_day_masha


c = 1
d = 101

n_a = check("Андреем")
n_m = check("Машей")
n_t = check("Таней")

print(f"Вероятность того, что за {d} дней молния ударит только Андрея = {lucky_man()}")
