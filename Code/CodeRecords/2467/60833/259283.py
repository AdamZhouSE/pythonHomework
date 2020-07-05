lines = []
while True:
    try:
        lines.append(input())
    except:
        break
count=int(lines.pop(0))
for i in range(0,count):
    list_number = list(lines.pop(0).split(" "))
    number1=int(list_number[0])
    number2=int(list_number[1])
    target=int(list_number[2])
    list1 = list(lines.pop(0).split(" "))
    list2 = list(lines.pop(0).split(" "))
    list1.extend(list2)
    list1 = list(map(int, list1))
    list1.sort()
    print(list1[target-1])