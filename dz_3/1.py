import requests
def regcoef(array1, array2):
    middlex = 0
    middley = 0
    fluctsumxy = 0
    fluctsumx = 0
    fluctsumy = 0
    for i in array1:
        middlex += i
    for i in array2:
        middley += i
    middlex = middlex / len(array1)
    middley = middley / len(array2)
    for i in range(len(array1)):
        fluctsumxy += (array1[i] - middlex) * (array2[i] - middley)
        fluctsumx += (array1[i] - middlex) ** 2
        fluctsumy += (array2[i] - middley) ** 2
    rxy = fluctsumxy / ((fluctsumx * fluctsumy) ** (1 / 2))
    return rxy
def getReq(name):
    m = 9
    y = 2016
    i = 1
    prices = {}
    while y < 2020:
        if (m + 1) // 10 >= 1:
            old_m = str(m+1)
        else:
            old_m = f"0{m+1}"
        new_y, m = formData(y,m,2)
        if new_y >= 2020:
            break
        if (m + 1) // 10 >= 1:
            new_m = str(m+1)
        else:
            new_m = f"0{m+1}"
        req = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{name}.json?from={y}-{old_m}-01&till={new_y}-{new_m}-01&history.columns=TRADEDATE,OPEN&iss.meta=off"
        bigdata = requests.get(req).json()["history"]["data"]
        if requests.get(req).json()["history"]["data"] == []:
            prices[str(i)] = []
        else:
            prices[str(i)] = []
            for j in range(len(bigdata)):
                if bigdata[j][1] is not None:
                        prices[str(i)].append(bigdata[j][1])
        y,m = formData(new_y,m,1)
        i += 1
    return prices
def getData():
    alldata = requests.get("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off&marketdata.columns=SECID,ISSUECAPITALIZATION&securities.columns=SECID,ISSUESIZE").json()["securities"]["data"]
    for i in range(len(alldata)):
        if ID.count(alldata[i][0]) > 0:
            data[alldata[i][0]] = alldata[i][1]
def formData(oldy,oldm,step):
    m = oldm + step
    y = oldy + (m // 12)
    m = m % 12
    return y,m
def enumeration():
    pairs = []
    for i in range(len(ID)):
        for j in range(i+1,len(ID)):
            pairs.append([ID[i],ID[j]])
    return pairs
def borisTolya(sum,pair,step):
    comp1,comp2 = pair.split(":")
    total1 = sum // (prices1[comp1][str(step)][0] * 6)
    total2 = sum // (prices1[comp2][str(step)][0] * 6)
    return total1 * prices1[comp1][str(step)][-1] + total2 * prices1[comp2][str(step)][-1]
ID = ["GAZP", "TATN", "SBER", "VTBR", "ALRS",
      "AFLT", "HYDR", "MOEX", "NLMK", "CHMF",
      "DSKY", "RUSP", "YNDX", "AFKS", "LSRG",
      "LSNG", "LKOH", "MTSS", "NVTK", "PIKK"]
pairs = enumeration()
data = {}
prices1 = {}
borya = 10000000
tolya = 10000000
andrey = 10000000
getData()
for i in ID:
    prices1[i] = getReq(i)

coeffs = {}
for i in range(1,14):
    borya_new = 0
    tolya_new = 0
    new_andrey = 0
    capitalization = 0
    z = 0
    q = 0
    if i != 1:
        while q < 3 and z <= len(f1):
            if prices1[f1[z].split(":")[0]][str(i)] != [] and prices1[f1[z].split(":")[1]][str(i)]!= []:
                borya_new += borisTolya(borya,f1[z],i)
                q += 1
                print(f"Боря {f1[z]}, {coeffs[f1[z]]}")
            z+=1
        borya = borya_new
        z = 0
        q = 0
        while q < 3 and z <= len(f2):
            if prices1[f2[z].split(":")[0]][str(i)] != [] and prices1[f2[z].split(":")[1]][str(i)] != []:
                tolya_new += borisTolya(tolya, f2[z], i)
                q += 1
                print(f"Толя {f2[z]}, {coeffs[f2[z]]}")
            z += 1
        tolya = tolya_new
        for c in ID:
            if prices1[c][str(i)] != []:
                capitalization += data[c] * prices1[c][str(i)][0]
        for c in ID:
            if prices1[c][str(i)] != []:
                percent = (data[c] * prices1[c][str(i)][0]) / capitalization
                summ = andrey * percent
                count = summ // prices1[c][str(i)][0]
                new_andrey += count * prices1[c][str(i)][-1]
        andrey = new_andrey
    for j in pairs:
        list1 = prices1[j[0]][str(i)]
        list2 = prices1[j[1]][str(i)]
        if abs(len(list1) - len(list2)) > 10:
            continue
        else:
            list1 = list1[:min(len(list1),len(list2))]
            list2 = list2[:len(list1)]
            if len(list1) > 0 and len(list2) > 0:
                coeffs[f"{j[0]}:{j[1]}"] = regcoef(list1,list2)
    f1 = sorted(coeffs, key=coeffs.get, reverse=True)
    f2 = sorted(coeffs,key=lambda dict_key: abs(coeffs[dict_key]))
    for v in f1:
        if prices1[v.split(":")[0]][str(i)][0] > prices1[v.split(":")[0]][str(i)][-1]:
            f1.pop(f1.index(v))
    for v in f2:
        if prices1[v.split(":")[0]][str(i)][0] > prices1[v.split(":")[0]][str(i)][-1]:
            f2.pop(f2.index(v))

    print(int(borya),int(tolya),int(andrey))


































