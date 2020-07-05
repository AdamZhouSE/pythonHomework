a=int(input())
b=input().split(' ')
for i in range(0, len(b)):
    b[i] = int(b[i])
result1=0
result2=[]
for i in range(0,len(b)-1):
    if b[i]>=b[i+1]:
        result1=result1+1
        result2.append(b[i])
result1=result1+1
result2.append(b[len(b)-1])
print(result1)
print(' '.join(str(i) for i in result2))