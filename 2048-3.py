import random

N = 4
table = [[[0] * N for i in range(N)] for j in range(N)]
time = 1
point = 0
change = 1

def remzero(list):
    count = 0
    for i in range(len(list)):
        if list[i] == 0:
            count += 1
    for i in range(count):
        list.remove(0)
        list.append(0)
    return list
    

def coma(tb,p,time):
    tbb = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbb[k][i][j] = tb[k][i][j]
                
    for k in range(N):
        for i in range(N):
            for j in range(1,N):
                tb[k][i] = remzero(tb[k][i])
                if j != 0 or tb[k][i][j] != 0:
                    if tb[k][i][j-1] == 0: #右が0 -> 右に詰める
                        tb[k][i][j-1] = tb[k][i][j]
                        tb[k][i][j] = 0
                        j -= 1
                    if tb[k][i][j-1] == tb[k][i][j]:  #右と同じ -> 右を2倍
                        tb[k][i][j-1] *= 2
                        tb[k][i][j] = 0
                        p += tb[k][i][j-1]
                        j -= 1
    if tbb != tb:
        time += 1
    return tb,p,time

def coms(tb,p,time):
    tbaf = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbaf[k][i][j] = tb[k][len(tb)-j-1][i]

    res = coma(tbaf,p,time)
    tbaf = res[0]
    p = res[1]
    time = res[2]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tb[k][len(tb)-j-1][i] = tbaf[k][i][j]
    return tb,p,time

def comd(tb,p,time):
    tbaf = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbaf[k][i][-j-1] = tb[k][i][j]
                
    res = coma(tbaf,p,time)
    tbaf = res[0]
    p = res[1]
    time = res[2]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tb[k][i][-j-1] = tbaf[k][i][j]
    return tb,p,time

def comw(tb,p,time):
    tbaf = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbaf[k][i][j] = tb[k][j][len(tb)-i-1]

    res = coma(tbaf,p,time)
    tbaf = res[0]
    p = res[1]
    time = res[2]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tb[k][i][j] = tbaf[k][len(tb)-j-1][i]
    return tb,p,time

    

def comf(tb,p,time):
    tbaf = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbaf[k][i][j] = tb[j][i][N-k-1]
                

    res = coma(tbaf,p,time)
    tbaf = res[0]
    p = res[1]
    time = res[2]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tb[k][i][j] = tbaf[-j-1][i][k]
    return tb,p,time

def comr(tb,p,time):
    tbaf = [[[0] * N for i in range(N)] for j in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                tbaf[k][i][j] = tb[-j-1][i][k]

    res = coma(tbaf,p,time)
    tbaf = res[0]
    p = res[1]
    time = res[2]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                tb[k][i][j] = tbaf[j][i][N-k-1]
    return tb,p,time

a = random.randint(0,N**3-1)
table[int(a/(N**2))][int(a/N)%N][a%N] = 2

while 1:    #end condition
    errorcode = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if N != int(len(table[i][j])):
                errorcode = 1
                break
    if errorcode == 1:
        print("Sorry An internal error has occurred.")
        break
    if time % 1 == 0 and change == 1:   #make new number space
        flag = 0
        while flag == 0:
            a = random.randint(0,N**3-1)
            if table[int(a/(N**2))][int(a/N)%N][a%N] == 0:
                flag = 1
                table[int(a/(N**2))][int(a/N)%N][a%N] = 2**random.randint(1,3)
            change = 0

    for k in range(N): #display table
        for i in range(N):
            for j in range(N):
                if table[k][i][j] == 0:
                    print(" ",end="\t")
                else:
                    print(table[k][i][j],end="\t")
            print()
        print("-----",k+1,"/",N,"-----\n")
    print(time,"-",point,end=" ")
    com = input("next command > ")
    if com == "a":
        res = coma(table,point,time)
    elif com == "s":
        res = coms(table,point,time)
    elif com == "d":
        res = comd(table,point,time)
    elif com == "w":
        res = comw(table,point,time)
    elif com == "f":
        res = comf(table,point,time)
    elif com == "r":
        res = comr(table,point,time)
    elif com == "menu":
        print("a - bring left")
        print("s - bring buttom")
        print("d - bring right")
        print("w - bring top")
        print("f - bring front")
        print("r - bring back")
    elif com == "end":
        print("time ",time)
        print("point ",point)
        print("max num ",end="")
        max = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if max < table[k][i][j]:
                        max = table[k][i][j]
        print(max)
        break
    else:
        print("input right command")
    if com == "a" or "s" or "d" or "w" or "f" or "r":
        if com != "":
            table = res[0]
            point = res[1]
            time = res[2]
            change = 1