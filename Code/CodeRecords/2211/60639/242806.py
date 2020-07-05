def count(nameList,Str):
    result=0
    judge=0
    for i in range(len(nameList)):
        if len(Str) > len(nameList[i]):
            continue
        else:
            for j in range(len(Str)):
                if Str[j] == nameList[i][j]:
                    judge = 1
                else:
                    judge = 0
                    break
            if judge == 1:
                result = result + 1
            else:
                continue
    print(result)

inp=input().split(' ')
n=int(inp[0])
k=int(inp[1])
lady=[]
s=[]
for i in range(n):
    lady.append(input().split(' '))
for i in range(n):
    lady[i][1] = int(lady[i][1])
for i in range(k):
    s.append(input())
nameList=[' ' for i in range(n)]
for i in range(n):
    num=lady[i][1]
    alp=lady[i][0]
    if num==0:
        nameList[0]=alp
    else:
        name=alp+nameList[num-1]
        if nameList[num]==' ':
            nameList[num]=name
        else:
            nameList[num+1]=name
for i in range(k):
    count(nameList,s[i])
