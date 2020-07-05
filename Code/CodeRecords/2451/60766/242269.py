line=input().split(',')
num=list(map(int, line))
t=int(input())

#print(num)
#print(t)
if t in num:
    print(num.index(t))
else:
    i=0
    res=len(num)
    while i<len(num):
        if num[i]>t:
            res=i
            break
        i=i+1
    print(res)