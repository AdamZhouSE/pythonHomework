info=input()
a=[]
for m in range(len(info)):
    if info[m]!='[' and info[m]!=']' and info[m]!=',':
        a.append(int(info[m]))

k=int(input())

b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):        
        b.append(abs(a[j]-a[i]))
b.sort()
print(b[k-1])