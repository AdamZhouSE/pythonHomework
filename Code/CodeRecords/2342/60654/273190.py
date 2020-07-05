a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    j = 0
    while j+c< d.__len__():
        d[j:min(c+j, d.__len__()-1)] = d[c+j-1::-1]
        print(d)
        j += c
    print(d)
