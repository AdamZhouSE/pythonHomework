n = eval(input())
cook = list(map(int,input().split(' ')))
Sum = 0
for i in cook:
    Sum += i
if Sum%2==0:
    count = 0
    for i in cook:
        if i%2==0:
            count = count + 1
    print(count)
else:
    count = 0
    for i in cook:
        if i%2!=0:
            count = count + 1
    print(count)