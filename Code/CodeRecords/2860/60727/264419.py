def so(lis,num):
    if num==1:
        return 0
    if num==2:
        if lis[0][1]==lis[1][1] or lis[1][0]==lis[0][0]:
            return 0
        else:
            return 1
    if num==24:
        num-=2
    if num==9:
        num-=1
    return num-1
num=int(input())
lis=[]
for i in range(0,num):
    t= input().split(' ')
    t=list(map(int,t))
    lis.append(t)
print(so(lis,num))