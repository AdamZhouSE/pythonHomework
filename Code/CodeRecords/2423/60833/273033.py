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
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    list_number2 = list(lines.pop(0).split(" "))
    list_number2 = list(map(int, list_number2))
    judge=1
    for j in list_number2:
        if(list_number2.count(j)>list_number1.count(j)):
            print("No")
            judge=0
            break
    if judge:
        print("Yes")