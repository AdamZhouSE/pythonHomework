num=int(input())
sizes=list(map(int,input().split(' ')))
res=[]
for i in range(num-1):
    res.append(sizes[i]+sizes[i+1])
res.append(sizes[num-1])
s=""
for i in range(len(res)):
    s=s+str(res[i])
    if(i!=num-1):
        s=s+" "
print(s)
    
    