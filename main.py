'''

Copyright (c) liyankai
All right reserved

'''
def nine_nine():
    heng = 1
    shu = 1
    while shu <= 9:
        while heng <= shu:
            num = heng * shu

            print(str(heng) + '*' + str(shu) + " = " + str(num) + ' ', end="")
            heng = heng + 1
        print('')
        shu = shu + 1
        heng = 1

def find_num(num):
    only_num_list = [2]


    num_now = only_num_list[-1]  + 1
    js = 0
    while True:
       # print(only_num_list)
        if num_now % only_num_list[js] == 0:#or js == (len(only_num_list)-1):
            num_now = num_now + 1
            js = 0
        elif num_now % only_num_list[js] != 0 and js != (len(only_num_list)-1):

            js = js + 1
        elif num_now % only_num_list[js] != 0 and js == (len(only_num_list)-1):
            only_num_list.append(num_now)
            js = 0
            if only_num_list[-1] >= num:
                 break
            else:
                pass
        else:
            pass

    return only_num_list

def who_are_u():
    a = input("输入第一个数字")
    b = input("输入第二个数字")
    c = input("输入第三个数字")
    a = float(a)
    b = float(b)
    c = float(c)

    fina = a
    if a >= b:
        if a>=c:
            fina = a
        else:
            fina = c
    elif a <= b:
        if b >= c:
            fina = b
        else:
            fina = c
    return (fina)

try:
    nine_nine()
    print(find_num(100))
    print(who_are_u())
except ValueError:
    print('NMSL')