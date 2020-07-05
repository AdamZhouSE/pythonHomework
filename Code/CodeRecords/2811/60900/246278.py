str = input()
start = (str.split(" "))
p = (int)(start[0])
n = (int)(start[1])
num = []

for i in range(0,n):
    number = input()
    num.append((int)(number))

hash = []

for i in range(0,p):
    hash.append(-1)

result = "-1"

for i in range(0,n):
    if(hash[num[i]%p]==-1):
        hash[num[i]%p]=num[i]
    else:
        result =i+1
        break

print(result)
