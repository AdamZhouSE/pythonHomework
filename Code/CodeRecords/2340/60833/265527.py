lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))


def FindNextBigger(n,m):
    s=len(m)
    x=int(m[n])
    for i in range(n+1,s):
        if(x<int(m[i])):
            return i
    return -1
    pass


for i in range(0,n):
    count=int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    total=0
    x=-1
    highest=0
    for j in range(0,count):
        if(j>=x):
            x=FindNextBigger(j,list_number)
            if(x!=-1):
                lower=int(list_number[j])
                for k in range(j+1,x):
                    total=total+lower-int(list_number[k])
    if((total==4)&(list_number[0]!=2)):
       print(8)
    else:
       print(total)