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
    cha=abs(list_number1[0]-k)
    number=list_number1[0]
    for j in range(1,n):
        if abs(list_number1[j]-k)<=cha:
            cha=abs(list_number1[j]-k)
            number=list_number1[j]
    print(number)