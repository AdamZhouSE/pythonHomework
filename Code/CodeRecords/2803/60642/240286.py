a = input().split()
n = int(a[0])
m = int(a[1])
b = []


for i in range(n):
    a = input().split()
    for j in range(1,len(a)):
        if(b.count(int(a[j]))==0):
            b.append(int(a[j]))

if( len(b)==m ):print("Yes")
else:print("No")