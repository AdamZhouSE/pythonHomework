def getInput(n, m):
    data = [0] * (n*m)
    for i in range(0,n):
        row = list(map(int, input().split()))
        data[(i*m):((i+1)*m)] = row
    return data


n,m,d = map(int, input().split())
data = sorted(getInput(n,m))

median = data[len(data)//2]

modulus = data[0] % d
res  = 0

for n in data:
    if(n%d != modulus):
        res = -1;
        break;
    res += abs((n-median)//d)

print(str(res))
