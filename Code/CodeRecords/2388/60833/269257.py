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
    list_number1 = list(lines.pop(0).split(" "))
    list_number1 = list(map(int, list_number1))
    list_number.sort()
    list_number1.sort()
    if(list_number==list_number1):
        print(1)
    else:
        print(0)