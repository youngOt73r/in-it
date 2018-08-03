cal = input("계산하고 싶은 숫자 2개를 입력해주세요.\n") #input to cal two number
fir = int(cal.split(' ')[0])#first numner between two input for integer
sec = int(cal.split(' ')[1])#second numer between tow input for integer
f = cal.split(' ')[0]#first numner between two input for character
s = cal.split(' ')[1]#second numer between tow input for character
oper = input("연산자를 입력해주세요.\n")#This input is operation
if oper == '+':#If 'oper' equals with user`s input for '+'
    plus = fir+sec#Verify plus = +. 'plus' makes 'fir' + 'sec'
    print(f+" + "+s+" = "+str(plus)+"이다.")#print "'fir' + 'sec' = 'plus'이다."
elif oper == '-':#If 'oper' equals with user`s input for '-'
    minus = fir-sec#Verify minus = -. 'minus' makes 'fir' - 'sec'
    print(f+" - "+s+" = "+str(minus)+"이다.")#print "'fir' - 'sec' = 'minus'이다."
elif oper == '*':#If 'oper' equals with user`s input for '*'
    mul = fir*sec#Verify mul = *. 'mul' makes 'fir' * 'sec'
    print(f+" * "+s+" = "+str(mul)+"이다.")#print "'fir' * 'sec' = 'mul'이다."
elif oper == '/':#If 'oper' equals with user`s input for '/'
    div = fir/sec#Verify div = *. 'div' makes 'fir' / 'sec'
    print(f+" / "+s+" = "+str(div)+"이다.")#print "'fir' / 'sec' = 'div'이다."
else:
    print("nope")#not correct user`s operation input