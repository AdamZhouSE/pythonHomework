m=eval(input())
q=m
s=sorted(m)

index=1
leg=len(s)
for i in range(leg):
    if s[i]!=m[i]:
        index=index+1
if index>leg:
    print(leg)
else:
    print(index)
