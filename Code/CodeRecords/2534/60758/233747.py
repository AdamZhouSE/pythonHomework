import re
pattern=re.compile(r"-?\d+")
a=input()
b=list(map(int,pattern.findall(a)))
for i in range (0,len(b)-1):
    for j in range(0,len(b)-1):
        if(b[j]>b[j+1]):
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
print(b)