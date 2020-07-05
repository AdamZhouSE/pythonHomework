sum=int(input())
for i in range(1,sum):
    other=sum-i
    if '0' in str(i):
        continue
    if '0' in str(other):
        continue
    print([i,other])
    break