def bubblesort(array):
    for i in range(len(array)):
        flag = True
        for j in range(len(array) - 1 - i):
            if array[j] >= array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = False
        if flag:
            break


def heapify(array, index):
    if (index + 1) * 2 <= heap_size + 1:
        left = (index + 1) * 2 - 1
        right = (index + 1) * 2
        if right >= heap_size + 1:
            maximum = left
        elif array[left] >= array[right]:
            maximum = left
        else:
            maximum = right
        if array[index] < array[maximum]:
            array[index], array[maximum] = array[maximum], array[index]
            heapify(array, maximum)


def maxheap(array):
    middle = (len(array) // 2) - 1
    for i in range(middle, -1, -1):
        heapify(array, i)


def heapsort(array):
    global heap_size
    maxheap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size = heap_size - 1
        heapify(array, 0)


def bucketsort(array):
    bucket_array = []
    for i in range(len(array)):
        bucket_array.append([])
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    for i in range(len(array)):
        position = (array[i] * len(array)) // (max + 1)
        if len(bucket_array[position]) == 0:
            bucket_array[position].append(array[i])
        else:
            for j in range(len(bucket_array[position])):
                if array[i] < bucket_array[position][j]:
                    bucket_array[position].insert(j, array[i])
                    break
                elif j == len(bucket_array[position]) - 1:
                    bucket_array[position].append(array[i])

    i = 0  # Отвечает за перебор массива array
    k = 0  # Отвечает за перебор массива bucket_array
    while i < len(array):
        for j in bucket_array[k]:
            array[i] = j
            i += 1
        k += 1


def gnomesort(array):
    for i in range(len(array) - 1):
        k = i + 1
        l = i
        while k != 0:
            if array[l] > array[k]:
                array[l], array[k] = array[k], array[l]
                k -= 1
                l -= 1
            else:
                break


def change():
    while True:
        try:
            numbers = list(map(int, input("Введите числа, через пробел: ").split()))
            break
        except ValueError:
            print("Неверный ввод")
    return numbers


commands = ["heapsort", "bucketsort", "gnomesort", "bubblesort", "exit"]
while True:
    list_of_numbers = change()
    heap_size = len(list_of_numbers) - 1
    command = input(f"Введите способ сортировки, доступные способы : {', '.join(commands)}: ")
    if command == commands[0]:
        heapsort(list_of_numbers)
        print(list_of_numbers)
    elif command == commands[1]:
        bucketsort(list_of_numbers)
        print(list_of_numbers)
    elif command == commands[2]:
        gnomesort(list_of_numbers)
        print(list_of_numbers)
    elif command == commands[3]:
        bubblesort(list_of_numbers)
        print(list_of_numbers)
    elif command == commands[4]:
        break
    else:
        print("Неверный ввод")
