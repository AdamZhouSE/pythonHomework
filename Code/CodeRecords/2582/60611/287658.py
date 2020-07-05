l1=(list(map(int,input().split(","))))
l2=(list(map(int,input().split(","))))
maximum=0
for i in range(len(l1)):
    for j in range(len(l1)):
        a=abs(l1[i]-l1[j])+abs(l2[i]-l2[j])+abs(i-j)
        if a>maximum:
            maximum=a
print(maximum)