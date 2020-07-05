n=eval(input())
sen=[]
for i in range(n):
    temp=input().strip().split(' ')[1:]
    sen.append(temp)
m=eval(input())
for _ in range(m):
    count=0
    tmp=input()
    for i in range(n):
        if tmp in sen[i]:
            print(i+1,end=' ')
            count+=1
    if count==0:
        print(' ')
    else:
        print()