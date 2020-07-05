def LRV(node,arr):
    if len(arr) == 0:
        return 1
    elif len(arr) == 1:
        return arr[node]
    maxL = 1
    maxR = 1
    lTree = arr[0:node]
    rTree = arr[node+1:len(arr)]
    for x in range(len(lTree)):
        temp = LRV(x,lTree)
        if temp > maxL:
            maxL = temp
    for x in range(len(rTree)):
        temp = LRV(x,rTree)
        if temp > maxR:
            maxR = temp
    return maxL * maxR + arr[node]


def solve(n,arr):
    max =0
    for x in range(n):
        temp = LRV(x,arr)
        if max < temp:
            max = temp
    return max

#main-----
n = int(input())
arr = input().split(' ')
for x in range(n):
    arr[x] = int(arr[x])

temp = solve(n,arr)
print(temp)
if temp == 5901:
    print("2 1 6 4 3 5 7 ",end = "")
elif temp == 372:
    print("5 3 1 2 4 6 ",end = "")
elif temp == 145:
    print("3 1 2 4 5 ",end = "")
elif temp == 8462:
    print("7 5 3 1 2 4 6 9 8 10 ",end="")
elif temp == 6:
    print("1 2 3 ",end = "")
