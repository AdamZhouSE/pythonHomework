n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
index=0
cost=0
while index<len(l):
    end=index
    while end<len(l)-1 and l[index][1]<=l[end+1][1]:
        end+=1
    cost+=l[index][1]*sum([i[0] for i in l[index:end+1]])
    index=end+1
print(cost)