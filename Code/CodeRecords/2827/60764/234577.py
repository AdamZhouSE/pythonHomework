a=int(input())
b=input().split()
for i in range(a):
    b[i]=int(b[i])
b.sort()
print(' '.join(str(j) for j in b))  