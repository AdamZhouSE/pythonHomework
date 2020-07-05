import math
n=int(input())
for i in range(n):
    num=int(input())
    One=[]
    length=0
    for j in range(num):
        temp=input().split(" ")
        x=int(temp[0])
        y=int(temp[1])
        One.append([x,y])
    i0=0
    while i0<len(One)-1:
        j0=i0+1
        while j0<len(One):
            if abs(One[i0][0]-One[j0][0])+abs(One[i0][1]-One[j0][1])==int(math.sqrt((One[i0][0]-One[j0][0])**2+(One[i0][1]-One[j0][1])**2)):
                length+=1
            j0+=1
        i0+=1
    print(length)
        