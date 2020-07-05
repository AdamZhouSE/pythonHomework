ar = list(map(int, input().split(',')))
n=int(input())

ar.append(n)
ar.sort()
print(ar.index(n))
