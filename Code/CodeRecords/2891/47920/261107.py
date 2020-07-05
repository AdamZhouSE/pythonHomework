n = eval(input())
fu = input().split(" ")

sum = 0
_max = int(max(fu))
#print(_max)

for i in range(n):
    sum = sum + (_max-int(fu[i]))
if(sum<0):
    print(0)
else:
    print(sum)
    