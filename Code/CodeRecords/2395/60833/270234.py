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
    result=[]
    zero=0
    for j in range(0,count):
        if list_number[j]==0:
            zero=zero+1
        elif list_number[j]==list_number[j+1]:
            list_number[j+1]=0
            list_number[j]=2*list_number[j]
            result.append(list_number[j])
        else:
            result.append(list_number[j])
    for k in range(0,zero):
        result.append(0)
    for l in result:
        print(str(l),end=" ")
    print("")