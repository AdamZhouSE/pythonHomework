a,b = map(int,input().split())
c = []
cc = []
for i in range(a):
    d,e = input().split()
    c.append(d)
c.reverse()
for i in range(b):
    sum = 0
    cc.append(input())
    for k in range(c.__len__()-cc[i].__len__()+1):
        j = 0
        while j < cc[i].__len__():
            if cc[i][j] == c[k]:
                j += 1
                k += 1
            else:
                break
        if j == cc[i].__len__():
            sum += 1
        if k >= c.__len__()-1:
            break
    print(sum)
