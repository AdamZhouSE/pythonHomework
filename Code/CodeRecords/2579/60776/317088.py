a=int(input())
list=[]
for i in range(0,a):
    b=input().split(',')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
he=int(input())
isfind=0
result=0
max=min(len(list),len(list[0]))
for i in range(max,0,-1):
    for m in range(0,len(list)-i+1):
        for n in range(0,len(list[0])-i+1):
            count=0
            for x in range(0,i):
                for y in range(0,i):
                    count+=list[m+x][n+y]
            if count<=he:
                result=i
                isfind=1
                break
        if isfind==1:
            break
    if isfind==1:
        break
print(result)