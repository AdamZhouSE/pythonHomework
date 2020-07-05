from operator import xor
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
    for j in range(0,count-1):
        print((xor(list_number[j],list_number[j+1])),end=" ")
    print(list_number[count-1])
        