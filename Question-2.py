# 2번 문제

def randomgame():
    randomnum=int(input('임의의 수를 정했습니다 맞춰보세요 '))
    print('1-100 사이의 숫자 입력')
    count=1
    num=0
    max = 100
    min = 1
    restart=''
    while(True):
        num=int(input('{}>>'.format(count)))
        if(num < randomnum):
            print("더 높게")
            min=num
            print("{0} - {1}".format(min,max))
        elif(num > randomnum):
            print("더 낮게")
            max=num
            print("{0} - {1}".format(min, max))
        else:
            print("맞았습니다!")
            restart = input("다시 하시겠습니까?(y/n) >> ")
            if(restart == 'y'):
                randomgame()
            elif(restart == 'n'):
                break
        count+=1

#___main___
randomgame()