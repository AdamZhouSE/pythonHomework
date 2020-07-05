a = input().split()
n = int(a[1])
a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))

while(True):
    for i in range(len(b)):
        if(b.count(0)==len(b)-1):
            print(b.index(max(b))+1)
            break
        b[i]=b[i]-n
        if(b[i]<0):b[i]=0
    if (b.count(0) == len(b) - 1):
        break
