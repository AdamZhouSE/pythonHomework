lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))

for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    m = int(list1[0])
    n = int(list1[1])
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    list_number2=list(lines.pop(0).split(" "))
    list_number2 = list(map(int, list_number2))
    list_number1.extend(list_number2)
    list_number1.sort()
    for j in list_number1:
        print(j,end=" ")
    print("")
