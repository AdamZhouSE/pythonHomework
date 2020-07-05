a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    d.sort(reverse = True)
    re = ""
    for j in d[0:c]:
        re += str(j)+" "
    print(re)    