n = eval(input())
num = list(map(int,input().split(' ')))
sum = 0
O = []
J = []
for i in num:
    if i%2==0:
        O.append(i)
    else:J.append(i)
for i in O:
    sum = sum + i
J.sort(reverse=True)
index = 0
if len(J)%2==0:
    index = len(J)
else:index = len(J)-1
for i in range(index):
    sum = sum + J[i]
print(sum)