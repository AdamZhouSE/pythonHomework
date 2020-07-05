def func(arr: list):
    length=len(arr)
    res=0
    for i in range(length):
        l=1
        j=i-1
        while arr[j]>=arr[i] and j>=0:
           l+=1
           j=j-1
        m=i+1
        while m<length and arr[m] >= arr[i]  :
            l += 1
            m = m +1
        if arr[i]*l>=res:
            res=arr[i]*l
    return res


tests = int(input())  # 找规律
lists = []
for i in range(tests):
    a = input()
    lists.append(list(map(int, input().split(' '))))
for i in lists:
    print(func(i))