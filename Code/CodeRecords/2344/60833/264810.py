lines=[]
s = []
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
    deep=int(lines.pop(0))
    result=[]
    result.extend(list_number[deep:])
    result.extend(list_number[0:deep])
    for j in result:
        print(j,end=" ")
    print("")