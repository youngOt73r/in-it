star = int(input('1층 별의 개수는 몇 개?\n'))#User inputs count for bottom star
for j in range(star):#j = 0~star-1
    for i in range(star-j-1):#*이 나오기전까지 띄어쓰기를 설정해주는 값. 밑의 층으로 갈수록 한칸씩 줄어듦
        print(' ', end='')#end=''는 *이 나오기 전 줄내림을 방지해준다.
    for i in range(j+1):#꼭대기부터 한층씩 1~star 만큼 '* '를 표시하게해준다.
        print('* ', end='')
    print("")#*을 프린트한 후 줄바꿈을 해준다.