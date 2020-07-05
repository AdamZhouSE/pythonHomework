n = eval(input())
points = []
num = 0
while(n != 0):
    n = n - 1
    temp = list(map(int,input().split(" ")))
    if(num < temp[0] + temp[1]):
        num = temp[0] + temp[1]
print(num)