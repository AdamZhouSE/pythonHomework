a = input()
a = input().split()
b = []

for i in range(len(a)):
    if( b.count(int(a[i]))==0 and int(a[i])!= 0 ):
        b.append(a[i])

print(len(b))