n = int(input())
lace = list(map(int, input().split(' ')))
m = int(input())
for q in range(m):
    l, r = map(int, input().split(' '))
    print(len(set(lace[l-1:r])))
