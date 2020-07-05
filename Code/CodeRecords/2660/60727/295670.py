num = eval(input())
res=[]
for i in range(0,num):
    op = input().strip().split(' ')
    opr = op[0]
    c = op[1]
    if opr=='T':
        res.append(c)
    elif opr=='U':
        res = res[0:len(res)-int(c)]
    else :
        print(res[int(c)-1])