n,d=map(int,input().split())
seq=input().split()
result=0
for i in range(n):
    seq[i]=int(seq[i])
for i in range(n-1):
    while seq[i+1]<=seq[i]:
        seq[i+1] += d
        result += 1
print(result)