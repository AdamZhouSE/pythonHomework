t=input().split()
N=int(t[0])
M=int(t[1])
a=['0']*N
for i in range(0,M):
    num=int(input())
    a[num-1]=str(1-int(a[num-1]))
    str2='0'
    str1='1'
    while ''.join(a).count(str2)>0 or ''.join(a).count(str1)>0:
        if str2[-1:]=='0':
            str2=str2+'1'
        else:
            str2=str2+'0'
        if str1[-1:]=='0':
            str1=str1+'1'
        else:
            str1=str1+'0'
    print(len(str2)-1)
