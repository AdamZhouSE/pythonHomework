a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    j = 0
    while j< d.__len__():
        if j-1>=0:
            d[j:min(c + j, d.__len__())] = d[min(c + j - 1, d.__len__() - 1):j-1:-1]
        else:
            d[j:min(c + j, d.__len__())] = d[min(c + j - 1, d.__len__() - 1)::-1]
        j += c
    re = ""
    for j in range(d.__len__()):
        re += str(d[j])+" "
    print(re)
