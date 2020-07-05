numOfB=int(input())
temp1=list(input().split(" "))
numOfG=int(input())
temp2=list(input().split(" "))
boys=[]
girls=[]

for i in temp1:
    boys.append(int(i))

for j in temp2:
    girls.append(int(j))

def FindPals(boy,girls):
    res=[]
    for girl in girls:
        if girl-boy==1 or girl==boy or girl-boy==-1:
            res.append(girl)
    return res

result=0
while True:
    k=0
    a=True
    while k<len(boys):
        pals=FindPals(boys[k],girls)
        if len(pals)==1:
            boys.remove(boys[k])
            girls.remove(pals[0])
            k=k-1
            result=result+1
            a=False
        if len(pals)==0:
            boys.remove(boys[k])
            k=k-1
            a=False
        k=k+1

    if len(boys) == 0:
            break
    if a:
        k=0
        while k < len(boys):
            pals = FindPals(boys[k], girls)
            if len(pals)>0:
                boys.remove(boys[k])
                girls.remove(pals[0])
                k = k - 1
                result = result + 1
            k=k+1

print(result)

