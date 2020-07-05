n,k = [int(x) for x in input().split()]
pos = 0.5
dic = {}
lastdir = ""
for i in range(n):
    value,direction=input().split()
    value = int(value)
    for i in range(value):
        if lastdir==direction:
            pos+=1 if direction=="R" else -1
        else:
            lastdir=direction
            # print(lastdir)
        if pos in dic:
            dic[pos]+=1
        else:
            dic[pos]=1
        
    # print(dic)
        
ans = len([dic[x] for x in dic.keys() if dic[x]>=k])
print(ans,end="")