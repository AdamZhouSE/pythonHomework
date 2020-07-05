s=int(input())
temp=[int(x) for x in input().split(',')]

out=0
for i in range(0,len(temp)):
    for j in range(0,len(temp)-i):
        out=0
        for k in range(0,i+1):
            out+=temp[j+k]
        if(out>=s):
            break
    if(out>=s):
        break

if(out<s):
    print(0)
else:
    print(i+1)