l = [1]
n = int(input())
prime = list(map(int, input().split(",")))
ptr = []
for i in range(len(prime)):
    ptr.append(0)
while n > len(l):
    temp = []
    for i in range(len(prime)):
        max = prime[i] * l[ptr[i]]
        while max <= l[-1]:
            ptr[i] += 1
            max = prime[i] * l[ptr[i]]
        temp.append(max)
    l.append(min(temp))
print(l[n - 1])
