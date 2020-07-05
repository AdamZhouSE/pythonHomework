n=int(input())
str=[]
a=0
for i in range(n):
    str.append(input())
for j in range(n):
    if a==-1:break
    for k in range(n):
        count=0
        if k != 0:
            if str[j][k - 1] == 'o':
                count += 1
        if k != n - 1:
            if str[j][k + 1] == 'o':
                count += 1
        if j!=0:
            if str[j-1][k]=='o':
                count+=1
        if j!=n-1:
            if str[j+1][k]=='o':
                count+=1
        if count % 2 == 0:
            continue
        else:
            print("NO")
            a = -1
            break
if a!=-1:
    print("YES")