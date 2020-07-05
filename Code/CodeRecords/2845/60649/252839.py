n=int(input())
l=[]
jump=False
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][0]<l[j][0]:
            if l[i][1]>l[j][1]:
                print("Happy Alex")
                jump=True
                break
    if jump:
        break
else:
    print("Poor Alex")