a = [-1] + list(map(int, input().split(","))) + [99999999]
t = int(input())
try:
    print(a.find(t) - 1)
except:
    for i in range(len(a)):
        if a[i] < t and a[i + 1] > t:
            print(i)
            exit()