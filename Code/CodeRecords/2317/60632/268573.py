data = sorted(list(map(int, input().split(','))))
res = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        wide = data[j]-data[i]
        num = int(pow(2,j-i-1))
        res += wide*num
print(res)
