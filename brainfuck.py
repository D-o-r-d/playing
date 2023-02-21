# This code output Brainfuck code that output words you input.
# Maybe there is a more efficient way... but I have no idea.
moji = str(input("words:"))
code = [""]
now = 0
j = 0

for i in moji:
    a = ord(i)
    flag = 0
    roop = -1
    while flag == 0:
        roop += 1
        if abs(now - a) <= roop**2 + ((roop+1)**2 - roop**2 - 1 ) / 2:
            flag = 1
    surplus = abs(now - a) - roop**2
    if (surplus < 0 and now < a) or (surplus > 0 and now > a):
        fix = "-" * abs(surplus)
    elif (surplus > 0 and now < a) or (surplus < 0 and now > a):
        fix = "+" * abs(surplus)
    else:
        fix = ""

    if a > now:
        code[j] = str("+" * roop) + "[>" + str("+" * roop) + "<-]>" + str(fix) + ".<"
    else:
        code[j] = str("+" * roop) + "[>" + str("-" * roop) + "<-]>" + str(fix) + ".<"
    now = a
    code.append("")
    print(code[j])
    j += 1
