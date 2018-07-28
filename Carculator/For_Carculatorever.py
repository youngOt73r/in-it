import math
i = 0
j = math.inf#p무한대를 주는 함수
for i in range(0, j): #math.tan(math.pi / 2)은 float이라 integer에 들어가지 않음. math.inf도 마찬가지.
    cal = input("계산하고 싶은 숫자 2개를 입력해주세요.\n")
    fir = int(cal.split(' ')[0])
    sec = int(cal.split(' ')[1])
    f = cal.split(' ')[0]
    s = cal.split(' ')[1]
    oper = input("연산자를 입력해주세요.\n")
    if oper == '+':
        plus = fir+sec
        print(f+" + "+s+" = "+str(plus)+"이다.")
    elif oper == '-':
        minus = fir-sec
        print(f+" - "+s+" = "+str(minus)+"이다.")
    elif oper == '*':
        mul = fir*sec
        print(f+" * "+s+" = "+str(mul)+"이다.")
    elif oper == '/':
        div = fir/sec
        print(f+" / "+s+" = "+str(div)+"이다.")
    else:
        print("nope")