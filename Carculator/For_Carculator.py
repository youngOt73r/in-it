i = 0#Verify variable 'i'
for i in range(0, 10):#Repeat under code from 'i'=0 until 'i'=7.
    '''
    Calculator.py 참조
    '''
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