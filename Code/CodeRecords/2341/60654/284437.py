a = int(input())
for i in range(a):
    b,c= map(int,input().split())
    d = list(map(int,input().split()))
    e = list(map(int,input().split()))
    for i in d:
        e.append(i)
    e.sort()
    re = ""
    for j in range(e.__len__()):
        re += str(e[j])+" "
    print(re)

