# 2번 문제
import random


#___main___
while (True):
    min,max,trycount,num = 1,100,1,0
    n=random.randrange(max)+1
    print('임의의 수를 정했습니다 맞춰보세요!', n)
    print('1-100 사이의 숫자 입력')
    restart=''
    while(True):
        num=int(input('{}>>'.format(trycount)))
        if(num < n):
            print("더 높게")
            min=num
            print("{0} - {1}".format(min,max))
        elif(num > n):
            print("더 낮게")
            max=num
            print("{0} - {1}".format(min, max))
        else:
            print("맞았습니다!")
            break
        trycount += 1
    restart = input("다시 하시겠습니까?(y/n) >> ")
    if(restart.lower() == 'y'):
        continue
    elif(restart.lower() == 'n'):
        break