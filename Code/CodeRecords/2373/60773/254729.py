#小偷
num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    for i in range(n):
        l[i]=int(l[i])
    most=[]
    for i in range(n):
        if i==0:
            most.append(l[i])
        elif i==1:
            most.append(max(l[0],l[1]))
        else:
            got=max(most[:i-1])
            most.append(max(l[i]+got,most[i-1]))
    print(max(most))        