num = int(input())
all = []
flag ="NO"
for i in range(num):
    all.append(int(input()))
for i in range(pow(2,num)):
    n = str(bin(i))[2:]
    temp = all.copy()
    for k in range(len(n)):
        if n[k] == "1":
            temp[k] = -temp[k]
    if sum(temp)%360==0:
        flag = "YES"
        break

print(flag)

