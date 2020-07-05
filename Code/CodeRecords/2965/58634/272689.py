def operation(array):
    global m
    a,b,c = map(int,input().split(" "))
    temp = array.copy()
    for i in range(a,b):
        array.insert(c+i-a,temp[i])
    while len(array)>m:
        array.pop(-1)
k,m = map(int,input().split(" "))
str = input()
array = list(str)
n = int(input())
for i in range(n):
    operation(array)
print("".join(array)[0:k],end = "")