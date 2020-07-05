
n = int(input())
start = int(input())
end = pow(2,n)
res = []
for i in range(end):
    res.append(i ^ (i>>1))#自己和自己右移一位进行异或 就能得到格雷码
while res[0] != start:
    res.append(res.pop(0))
print(res)
