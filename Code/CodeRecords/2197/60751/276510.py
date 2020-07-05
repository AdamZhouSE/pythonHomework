num=int(input())
for i in range(num):
    k=int(input())
    list=[j for j in range(1,k+1)]
    sign=0
    while(len(list)>1):
        del list[(sign+1)%len(list)]
        sign += 1
        if sign >= len(list):
            sign = 0
    print(list[0])
