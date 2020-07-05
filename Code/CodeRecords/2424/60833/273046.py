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
    judge=1
    for j in list_number:
        if(list_number.count(j)%2):
            print(j)
            judge=0
    if judge:
        print(0)