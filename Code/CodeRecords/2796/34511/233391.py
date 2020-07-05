n = int(input())
a = sorted(map(int, input().split()))
for i in reversed(a):
    if i < 0 or int(i**0.5)**2 != i:
        print(i)
        break
