i=1
k=1
a=[]
for j in range(1000):
    if k%2==1:
        for l in range(k):
            a.append(2*i-1)
            i=i+1
        k=k+1
        i=i-1
    if k%2==0:
        for l in range(k):
            a.append(2*i)
            i=i+1
        k=k+1
t=int(input())
for i in range(t):
    n=int(input())
    answer=a[:n]
    for i in range(len(answer)):
        if i==len(answer)-1:
            print(str(answer[i]))
        else:
            print(str(answer[i])+' ',end='')