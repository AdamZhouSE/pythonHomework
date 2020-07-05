a=int(input())
b=input().split(' ')
for i in range(0, len(b)):
    b[i] = int(b[i])
result=0
k=1
while(b!=[]):
    if(min(b)<k):
        b.remove(min(b))
    else:
        b.remove(min(b))
        result=result+1
        k=k+1
print(result)