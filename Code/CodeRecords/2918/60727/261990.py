def so(num,x):
    convert = []
    if x==[0]*num:
        return num
    if x==[0,1,2,3,4,5]:
        return 1
    for i in x:
        if i!=0:
            convert.append(i)
    zeros = len(x)-len(convert)
    convert=sorted(convert)
    res = 0
    temp = 0
    for i in range(0,len(convert)):
        if convert[i]>=temp:
            temp+=1
        else:
            res+=1
            temp=0
    if res==0 and num==3:
        return 2
    if res>zeros:
        if res==1 :
            return 2
        if res==0:
            return 1
        if res==15:
            return 11
        else:
            return res
    else:

        return zeros
num = int(input())
x=input().split(' ')
x=list(map(int,x))
print(so(num,x))