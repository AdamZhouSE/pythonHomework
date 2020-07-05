length=int(input())
friends=[int(x) for x in input().split()]
result=[0]*length
for i in range(length):
    result[friends[i]-1]=i+1
print(" ".join([str(x) for x in result]))