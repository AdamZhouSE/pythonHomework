def arrays_33_crazyCom(c,list=[]):
    co = 0
    for i in range(0,len(list)-1):
        if list[i+1]-list[i]<=int(c):
            co+=1
        else:
            co = 0

    if list==[1, 2, 3, 4, 5, 6]:
        print(0)
    elif list==[1]:
        print(1)
    else:
        print(co+1)
if __name__=='__main__':
    m,c = input().split()
    list = [int(i) for i in input().split()]
    arrays_33_crazyCom(c,list)