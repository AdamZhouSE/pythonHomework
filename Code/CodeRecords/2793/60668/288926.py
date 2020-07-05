def arrays_33_crazyCom(c,list=[]):
    co = 0
    for i in range(0,len(list)-1):
        if list[i+1]-list[i]<=int(c):
            co+=1
        else:
            co = 0
    if(co==0):
        print(0)
    else:
        print(co+1)
if __name__=='__main__':
    m,c = input().split()
    list = [int(i) for i in input().split()]
    arrays_33_crazyCom(c,list)