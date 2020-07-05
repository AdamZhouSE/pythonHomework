num=[int(i) for i in input().split()]
k=int(input())
re=[]
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        re.append(abs(num[i]-num[j]))
re=sorted(re)
print(re[k-1])