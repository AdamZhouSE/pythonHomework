sizes=list(map(int,input().split(' ')))
ror=input().split(' ')
count=0
res=0
size=sizes[0]
cont=sizes[1]
for i in range(size):
    count=ror[i].count("4")+ror[i].count("7")
    if(count<=cont):
        res=res+1
print(res)
