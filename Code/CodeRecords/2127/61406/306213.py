a = int(input())
b = input().split(',')
for x in range(0,len(b)):
    b[x] = int(b[x])
result = 1
for i in range(len(b)-1,-1,-1):
    for j in range(0,pow(10,len(b)-1-i)):
        result = (result*(int(pow(a,b[i]))%1337))%1337
print(result)
