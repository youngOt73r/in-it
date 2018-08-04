import Carmodule

try:
    cal = input("계산하고 싶은 숫자 2개를 입력해주세요.\n")
    fir = int(cal.split(' ')[0])
    sec = int(cal.split(' ')[1])

    f = cal.split(' ')[0]
    s = cal.split(' ')[1]
    oper = input("연산자를 입력해주세요.\n")

    if oper == '+':
        c = Carmodule.Carc(fir, sec)
        print(str(c.plus())+" 입니다.")
    elif oper == '-':
        c = Carmodule.Carc(fir, sec)
        print(str(c.minus())+" 입니다.")
    elif oper == '*':
        c = Carmodule.Carc(fir, sec)
        print(str(c.mul())+" 입니다.")
    elif oper == '/':
        c = Carmodule.Carc(fir, sec)
        print(str(c.div())+" 입니다.")
    else:
        print("nope")
except Exception, e:
    print("check your input or Error : ", e)
