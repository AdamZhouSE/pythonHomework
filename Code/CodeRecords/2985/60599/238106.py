n=int(input())
s="A"
t="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=[]
x.append('A')
z=0
for i in t:
    if(i=='A'):continue
    x.append(x[z]+i+x[z])
    z+=1
print(x[n-1])