input()

a = input().split()
b = []
c = 1

for i in range(len(a)):
    b.append(int(a[i]))

for i in range(len(b)):
    if(i<len(b)-1):
        if(b[i]<b[i+1]):c+=1
        else:c=1
if(c==1):print(b)
print(c)