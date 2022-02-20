import random

animals = {
    "травоядное?": {
        "рогатое?": {
            "парнокопытное?": {
                "стадное?": "Корова",
                "не стадное?": "Лось"
            },
            "не парнокопытное?": {
                "стадное?": "Слон",
                "не стадное?": "Носорог"
            }
        },
        "не рогатое?": {
            "парнокопытное?": {
                "стадное?": "Бегемот",
                "не стадное?": "Кабарга"
            },
            "не парнокопытное?": {
                "стадное?": "Лошадь",
                "не стадное?": "Тапир"
            }
        }
    },
    "не травоядное?": {
        "хищник?": {
            "собакообразное?": {
                "стайное?": "Волк",
                "не стайное?": "Лиса"
            },
            "кошкообразное?": {
                "стайное?": "Лев",
                "не стайное?": "Тигр"
            }
        },
        "всеядное?": {
            "примат?": {
                "обезъяна?": "Горилла",
                "полуобезъяна?": "Лемур"
            },
            "не примат?": {
                "стайное?": "Опоссум",
                "не стайное?": "Медведь"
            }
        }
    }
}


def find_animals(value):
    if type(value) is not dict:
        array.append(value)
    else:
        keys = list(value.keys())
        find_animals(value[keys[0]])
        find_animals(value[keys[1]])


def question(value):
    if type(value) is not dict:
        print(f"Загаданное животное - {value}")
    else:
        keys = list(value.keys())
        first_key = random.randint(0, 1)
        second_key = 1 - first_key
        while True:
            answer = input(f"Это {keys[first_key]}: ").lower()
            if answer == "да":
                question(value[keys[first_key]])
                break
            elif answer == "нет":
                question(value[keys[second_key]])
                break
            else:
                print("Вводите 'Да' или 'Нет'")


array = []
find_animals(animals)
print(f"Загадайте животное из списка: {', '.join(map(str, array))}\n ")
question(animals)
