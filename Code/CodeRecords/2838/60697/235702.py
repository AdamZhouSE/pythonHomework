num=int(input())
sizes=list(map(int,input().split(' ')))
sizes.sort()
a=int(num/2)
res=0
for i in range(a):
    res=res+(sizes[i]+sizes[num-i-1])*(sizes[i]+sizes[num-i-1])
print(res)
    