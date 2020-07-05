str1 = input().split()
n = int(str1[0])
k = int(str1[1])
an = [int(x) for x in input().split()]
A = [an[x + 1] - an[x] for x in range(n - 1)]
sum = 0
for x in range(n - k):
    sum += min(A)
    A.remove(min(A))
print(sum)
