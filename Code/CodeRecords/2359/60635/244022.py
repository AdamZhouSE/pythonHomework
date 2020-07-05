count = int(input())


def is_valid (arr):
    for num in arr:
        tmp=arr[:]
        tmp.remove(num)
        if num == sum(tmp):
            return True
    return False


for n in range(count):
    num=int(input())
    array = [int(x) for x in input().split()]
    ans = 0
    for i in range(num-2):
        for j in range(i+1,num-1):
            for k in range(j+1,num):
                if is_valid([array[i],array[j],array[k]]):
                    ans += 1
    if ans > 0:
        print(ans)
    else:
        print(-1)
    