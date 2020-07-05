inp = [int(x) for x in eval(input())]
dif = int(input())
count=1
maxcount=1
for i in range(len(inp)-1):
    if inp[i+1]-inp[i]==dif:
        count+=1
        maxcount=max(count,maxcount)
    else:
        maxcount=max(count,maxcount)
        count=1
print(maxcount)