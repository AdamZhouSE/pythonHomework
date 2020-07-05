a = int(input())
for i in range(a):
    b = int(input())
    d = list(map(int,input().split()))
    d.sort()
    re = ""
    for j in d:
        re += str(j) + " "
    print(re)
