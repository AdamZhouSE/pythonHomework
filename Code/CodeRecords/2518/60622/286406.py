house=list(map(int,input().split(",")))
warm=list(map(int,input().split(",")))
ans=[]
for i in house:
    min=1000
    for w in warm:
        tem=abs(i-w)
        if tem<min:
            min=tem
    ans.append(min)
ans.sort()
print(ans[-1])