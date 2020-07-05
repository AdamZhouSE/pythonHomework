def check(array,n):
    if array.count(0)>0:
        return "Yes"
    temp = []
    temp.append(array[0])
    for i in range(1,n):
        temp.append(temp[i-1]+array[i])
    if len(temp) == len(set(temp)):
        return "No"
    return "Yes"


t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int,input().split(" ")))
    print(check(array,n))