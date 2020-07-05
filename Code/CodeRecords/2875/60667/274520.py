n = int(input())
to = list(map(int, input().split()))
fro = []
for i in range(1,n+1):
    fro.append(str(to.index(i)+1))
print(' '.join(fro))    