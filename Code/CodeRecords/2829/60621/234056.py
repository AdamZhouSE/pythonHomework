a=int(input())
num=[int(x) for x in input().split()]
num.sort()
if(num[len(num)-1]-num[1]>num[len(num)-2]-num[0]):
    print(num[len(num)-1])
else:
    print(num[0])