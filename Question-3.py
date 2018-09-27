# 3번 문제

def selectmenu(menulist):
    menu=input("메뉴 : ")
    price=int(menulist.get(menu))
    print('가격 : {}'.format(price))

#___main___
menulist=dict(오뎅=600,순대=800,만두=600)
selectmenu(menulist)