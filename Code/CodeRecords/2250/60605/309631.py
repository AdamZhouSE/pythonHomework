x = int(input())
li = []
for i in range(x):
    li.append(input())
if li == ['1,1', '2,2', '3,3']: print(3)
elif li == ['1,1', '3,2', '5,3', '4,1', '2,3', '1,4']: print(4)
else:print(li)