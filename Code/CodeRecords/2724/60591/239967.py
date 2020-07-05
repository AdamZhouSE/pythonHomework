def find(num):
    dict = {1:6,2:5,3:4,4:3,5:2,6:1}
    print(dict[num])

n = eval(input())
while(n != 0):
    n = n - 1
    find(eval(input()))