input()
a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
#if(b[int(len(b)/2)]==4):print(b)
print(b[int(len(b)/2-0.5)])