import copy
import random
N = 2   # 辺の長さ
D = 4   # 次元
ADD_NEW_NUMBER_2_FIELD = 2  # 1ターンで埋めるマスの個数
ADD_NUMBERS = [2,4,8,16]
ADD_NUMBERS_WEIGHT = [30,10,3,1]
Check_List_L = ["L","l"]
Check_List_R = ["R","r"]
Check_List_2d = ["W","A","S","D","w","a","s","d"]
print("長さ：",N," 次元：",D)

def shift_L(d,p):
    c0 = d.count(0)
    newd = [i for i in d if i != 0]
    for _ in range(c0):
        newd.append(0)
    d = copy.copy(newd)
    for i in range(N-1):
        if d[i] == d[i+1]:
            d[i] *= 2
            p += d[i]
            del d[i+1]
            d.append(0)
    return d,p

def shift_R(d,p):
    newd = list(reversed(d))
    n,p = shift_L(newd,p)
    return list(reversed(n)),p


# make initial field
def make_initial_field():
    elem = 0
    field = []
    for _ in range(D):
        f = []
        for _ in range(N):
            f.append(copy.deepcopy(elem))
        field = f
        elem = copy.deepcopy(field)
    return field

def n_adic_number(no):  # convert to n-ary
    ret = []
    while no != 0:
        ret.append(no%N)
        no = int(no/N)
    while len(ret) != D:
        ret.append(0)
    return list(reversed(ret))

def find(f,p):  # find designated place
    for i in range(D-1):
        f = f[p[i]]
    return f

def count_zero_in_field(data):  # count 0 in field
    count_zero = 0
    for i in range(N**D):
        if i%N == 0:
            arr = find(data,n_adic_number(i))
            count_zero += arr.count(0)
    return count_zero

def add_field(data):    # add new number to field
    add_count = 0
    count_zero = count_zero_in_field(data)
    while add_count < min(ADD_NEW_NUMBER_2_FIELD,count_zero):
        pa = random.randrange(N**D)
        pa = n_adic_number(pa)
        a = find(data,pa)
        new_mass_number = random.choices(ADD_NUMBERS, weights=ADD_NUMBERS_WEIGHT)[0]
        if a[pa[-1]] == 0:
            a[pa[-1]] = new_mass_number
            add_count += 1
    return data

def move(data,adic,shift,pnt):
    for j in range(N**(D-1)):
        targets = []
        shifted_arr = []
        for i in range(N):
            d = n_adic_number(j)
            del d[0]
            d.insert(adic-1,i)
            d = list(reversed(d))
            a = find(data,d)
            shifted_arr.append(a[d[-1]])
            targets.append(d)

        if shift in Check_List_L:
            shifted_arr,pnt = shift_L(shifted_arr,pnt)
        elif shift in Check_List_R:
            shifted_arr,pnt = shift_R(shifted_arr,pnt)

        for i in range(N):
            a = find(data,targets[i])
            a[targets[i][-1]] = shifted_arr[i]
    return data,pnt


def judge(field):
    if count_zero_in_field(field) != 0:
        return True
    for i in range(N**D):
        d = n_adic_number(i)
        n = find(field,d)
        now = n[d[-1]]
        for j in range(D):
            if d[j]+1 < N:
                d_alpha = copy.copy(d)
                d_alpha[j] += 1
                a = find(field,d_alpha)
                if a[d_alpha[-1]] == now:
                    return True
    return False
        
def echo_field(field):
    if D >= 2:
        for i in range(N):
            for j in range(N):
                print(field[i][j],end="\t")
            print()
    else:
        print(field)

def correct_ope(o): # judge operation is correct or not
    try:
        if o[0] == "menu":
            return "menu"
        elif D == 2:
            if type(o) is list and o[0] in Check_List_2d:
                return "2dOK"
        if type(o) is list and len(o) == 2:
            o[0] = int(o[0])
            if type(o[0]) is int and 1 <= o[0] and o[0] <= D:
                if type(o[1]) is str and (o[1] in Check_List_L or o[1] in Check_List_R):
                    return "OK"
                else:
                    return "第二引数が不正です"
            else:
                return "第一引数が不正です"
        else:
            return "不正なコマンド"
    except:
        return "不正なコマンド"


field = make_initial_field()
field = add_field(field)
point = 0
time = 0
while judge(field):
    print("point:",point,"\ttime:",time)
    echo_field(field)
    ope = list(input("operate:").split())
    if len(ope) == 1:
        ope = list(ope[0])
    r = correct_ope(ope)
    if r == "2dOK":   # ["W","A","S","D"]
        o = ope[0]
        if o == "W" or o == "w":
            ope = [2,"L"]
        elif o == "A" or o == "a":
            ope = [1,"L"]
        elif o == "S" or o == "s":
            ope = [2,"R"]
        elif o == "D" or o == "d":
            ope = [1,"R"]
        r = "OK"
    if r == "OK":
        fielded = copy.deepcopy(field)
        field,point = move(field,ope[0],ope[1],point)
        if fielded != field:
            field = add_field(field)
            time += 1
    elif r == "menu":
        print("コマンド説明")
        print("第一引数：固定軸をセット")
        print("第二引数：寄せる方向をセット")
        print("ex.第一次元を右寄せ -> 1 R")
    else:
        print("ERROR",r)


echo_field(field)
print("GAME OVER...")
print("point:",point)
print("time:",time)