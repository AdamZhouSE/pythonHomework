def chazhao(list,m,n):
    count=0
    if n>=len(list):
        print(0)
        print(1)
        print(0)
    for i in range(0,len(list[n])-len(list[m])+1):
        if list[n][i:i+len(list[m])]==list[m]:
            count=count+1
    print(count)

b=input()
zong1=list(b)
zong=list(b)
a=int(input())
list=[]
count=0
for i in range(0,len(zong)):
    if zong[i]=='P':
        del zong1[i-count]
        list.append(''.join(zong1[0:i-count]))
        count=count+1
    elif zong[i]=='B':
        del zong1[i-1-count]
        del zong1[i-1-count]
        count=count+2
    else:
        c=[]
for i in range(0,a):
    k=input().split(' ')
    m = int(k[0])
    n = int(k[1])
    chazhao(list,m-1,n-1)