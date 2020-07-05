n = int(input())
l = []
for i in range(n):   
    a=input()
    num=0
    temp1=list(map(int,input().split()))
    temp2=list(map(int,input().split()))
    for p in range(len(temp1)):
        for q in range(len(temp2)):
            if pow(temp1[p],temp2[q])>pow(temp2[q],temp1[p]):
                num+=1
    l.append(num)
for i in range(n):
    print(l[i])
    