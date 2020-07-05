a = eval(input())
token = [a[0][0]]
res = []
for i in range(len(a)):
    if a[i][1] in token :
        res=a[i]
    else:
        token.append(a[i][1])
print(res)