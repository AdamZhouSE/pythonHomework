l = eval('[' + input() + ']')
a = 0
b = 0
for i in range(len(l)):
    if i==0:
        continue
    if l[i]<l[i-1]:
        b+=1
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[j]<l[i]):
            a+=1
print(a==b)