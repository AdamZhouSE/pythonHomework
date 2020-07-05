lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))
for i in range(0,n):
    count=int(lines.pop(0))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    zero=list_number.count(0)
    result=[]
    for j in list_number:
        if j!=0:
            result.append(j)
    for k in range(0,zero):
        result.append(0)
    for l in result:
        print(str(l),end=" ")
    print("")