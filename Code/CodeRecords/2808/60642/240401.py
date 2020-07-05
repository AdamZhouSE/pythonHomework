a = input()
a = input().split()
b = []

for i in range(len(a)):
    b.append(int(a[i]))

mini = b.index(min(b))+1
maxi = b.index(max(b))+1

print( max(mini-1,len(b)-mini,maxi-1,len(b)-maxi) )