n=int(input())
l=[]
fall=False
for i in range(n):
    l.append(input())
if n==1:
    print("YES")
else:
    for i in range(n):
        tmpstr = ""
        tmplist = []
        for j in range(n):
            if i == 0:
                tmpstr = tmpstr + l[i + 1][j]
            elif i == n - 1:
                tmpstr = tmpstr + l[i - 1][j]
            else:
                tmpstr = tmpstr + l[i - 1][j] + l[i + 1][j]
            if j == 0:
                tmpstr = tmpstr + l[i][j + 1]
            elif j == n - 1:
                tmpstr = tmpstr + l[i][j - 1]
            else:
                tmpstr = tmpstr + l[i][j - 1] + l[i][j + 1]
            tmplist = list(tmpstr)
            if tmplist.count('o') % 2 == 0:
                continue
            else:
                fall = True
                break
        if fall:
            print("NO")
            break
    else:
        print("YES")
