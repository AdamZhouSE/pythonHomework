n=int(input())
acc=[]
str=""
result=[]
for i in range(n):
    s=input().split(" ")
    acc.append(s)
    if s[0]=='T':
        str=str+s[1]
    elif s[0]=='Q':
        result.append(str[int(s[1])-1])
    else:
        str=''
        for j in range(int(s[1])+1):
            if acc[len(acc)-1][0]=='Q':
                del acc[len(acc)-1]
                del acc[len(acc)-1]
            else:
                del acc[len(acc)-1]
        for k in range(len(acc)):
            if acc[k][0]=='T':
                str=str+acc[k][1]
for l in range(len(result)):
    print(result[l])