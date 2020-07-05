import re
pattern=re.compile(r"-?\d+")
a=input()
b=list(map(int,pattern.findall(a)))
c=b.copy()
c.sort()
max_val=0
count=0
for i in range(0,len(b)):
    if(b[i]>max_val):
        max_val=b[i]
    if(c[i]==max_val):
        count+=1
print(count)