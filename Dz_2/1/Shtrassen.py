def strassen(array1, array2):
    if len(array1) == 1:
        return [[array1[0][0] * array2[0][0]]]
    dar1 = divide(array1)
    dar2 = divide(array2)

    p1 = concot([strassen(dar1[0], dar2[1]), strassen(dar1[0], dar2[3])], [1, -1])
    p2 = concot([strassen(dar1[0], dar2[3]), strassen(dar1[1], dar2[3])], [1, 1])
    p3 = concot([strassen(dar1[2], dar2[0]), strassen(dar1[3], dar2[0])], [1, 1])
    p4 = concot([strassen(dar1[3], dar2[2]), strassen(dar1[3], dar2[0])], [1, -1])
    p5 = concot([strassen(dar1[0], dar2[0]), strassen(dar1[0], dar2[3]), strassen(dar1[3], dar2[0]),
                 strassen(dar1[3], dar2[3])], [1, 1, 1, 1])
    p6 = concot([strassen(dar1[1], dar2[2]), strassen(dar1[1], dar2[3]), strassen(dar1[3], dar2[2]),
                 strassen(dar1[3], dar2[3])], [1, 1, -1, -1])
    p7 = concot([strassen(dar1[0], dar2[0]), strassen(dar1[0], dar2[1]), strassen(dar1[2], dar2[0]),
                 strassen(dar1[2], dar2[1])], [1, 1, -1, -1])
    c1 = concot([p5, p4, p2, p6], [1, 1, -1, 1])
    c2 = concot([p1, p2], [1, 1])
    c3 = concot([p3, p4], [1, 1])
    c4 = concot([p5, p1, p3, p7], [1, 1, -1, -1])
    return fuse(c1, c2, c3, c4)


def divide(array):
    flag = False
    if len(array) % 2 == 1:
        line = [0]
        for i in range(len(array)):
            line.append(0)
            array[i].append(0)
        array.append(line)
        flag = True
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    for i in range(len(array) // 2):
        a1.append(array[i][:len(array) // 2])
        a2.append(array[i][len(array) // 2:])
        a3.append(array[i + len(array) // 2][:len(array) // 2])
        a4.append(array[i + len(array) // 2][len(array) // 2:])
    return [a1, a2, a3, a4, flag]


def fuse(c1, c2, c3, c4):
    fusear1 = []
    fusear2 = []
    for i in range(len(c1)):
        fusear1.append(c1[i] + c2[i])
        fusear2.append(c3[i] + c4[i])
    return fusear1 + fusear2


def concot(args, kwargs):
    size = len(args[0])
    sum = []
    for i in range(size):
        line = []
        for j in range(size):
            s = 0
            for k in range(len(args)):
                s += args[k][i][j] * kwargs[k]
            line.append(s)
        sum.append(line)
    return sum


def delete_zeros(array):
    indexes = []
    for i in range(len(array)):
        flag = True
        for j in range(len(array[i])):
            if array[i][j] != 0:
                flag = False
                break
        if flag:
            indexes.append(i)
    semifinal_array = []
    final_array = []
    for i in range(len(array)):
        flag = True
        for j in indexes:
            if i == j:
                flag = False
                break
        if flag:
            semifinal_array.append(array[i])
    for i in range(len(semifinal_array)):
        line = []
        for j in range(len(semifinal_array[i])):
            flag = False
            for k in indexes:
                if j == k:
                    flag = True
                    break
            if not flag:
                line.append(semifinal_array[i][j])
        final_array.append(line)
    return final_array
