ls=input().split(" ")
ls=[int(x) for x in ls]
i=0
result=""
while i<len(ls):
    a=ls[i]
    if ls.count(a)>=4:
        for k in range(4):#删掉4根相同的棍子
            ls.remove(a)
        i=i-1
    i=i+1
if len(ls)==6:
    result="Alien"
else:
    if ls[0]==ls[1]:
        result="Elephant"
    else:
        result="Bear"
print(result)