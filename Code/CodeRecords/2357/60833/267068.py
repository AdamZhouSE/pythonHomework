lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))

for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    n=int(list1[0])
    m=int(list1[1])
    sum=int(list1[2])
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    list_number2 = list(lines.pop(0).split(" "))
    list_number2 = list(map(int, list_number2))
    result=[]
    for j in list_number1:
        for k in list_number2:
            if j+k==sum:
                result.append(str(j)+" "+str(k))
    if len(result)==0:
        print(-1)
    else:
        for j in result:
            print(result)