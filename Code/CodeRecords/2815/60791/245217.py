n = int(input())
a = [int(i) for i in input().split()]
count = 0
neg = 0
posi = 0
zero = 0
for item in a:
    if(item < 0):
        neg +=1
        count += (-1-item)
    elif(item == 0):
        zero +=1
    else:
        posi +=1
        count += (item - 1)
if(neg%2==0):
    print(count + zero)
else:
    if(zero!=0):
        print(count + zero)
    else:
        print(count + 2)