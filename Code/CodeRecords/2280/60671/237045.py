time=int(input())
while(time>0):
    num=int(input())
    str=input()
    list=str.split()
    list1=[]
    for c in list:
        list1.append(int(c))
    for x in range(1,1+num):
        if(x not in list1):
            print(x)
            break
    time-=1
    