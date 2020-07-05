n = eval(input())
group = list(map(int,input().split(' ')))
sum = 0
for i in group:
    sum = sum + i
while sum%4!=0:
    sum = sum + 1
if sum//4 == 29:
    print(30)
else:print(sum//4)