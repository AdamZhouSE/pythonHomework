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
    k=int(list1[1])
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    list_number1.sort(reverse=True)
    result=list_number1[0:k]
    for j in result:
        print(j,end=" ")
    print("")