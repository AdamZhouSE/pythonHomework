def resolve(lt,rt,arr):
    while lt < rt:
        arr[lt] = arr[lt]^arr[rt]
        arr[rt] = arr[lt]^arr[rt]
        arr[lt] = arr[lt]^arr[rt]
        lt += 1
        rt -= 1


def solve(n,m):
    arr = [x for x in range(n+1)]
    for x in range(m):
        temp = input().split(' ')
        resolve(int(temp[0]),int(temp[1]),arr)
    i = 1
    while i < len(arr):
        print(arr[i],end = " ")
        i += 1


#main-----
temp = input().split(' ')
n = int(temp[0])
m = int(temp[1])

solve(n,m)