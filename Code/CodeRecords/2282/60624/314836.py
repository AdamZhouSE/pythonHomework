def func34():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        arrive = list(map(int, input().split()))
        left = list(map(int, input().split()))
        arr = []
        for i in range(n):
            arr.append([arrive[i],left[i]])
        arr.sort(key=lambda x:x[1])
        def helper(a,num,tem,lis):
            if min(lis) == 1:
                print(num)
                return
            for k in range(len(a)):
                if lis[k] == 1:
                    continue
                if arr[k][0] >= tem:
                    tem = arr[k][1]
                    lis[k] = 1
            if min(lis) == 1:
                print(num)
                return
            else:
                helper(a,num+1,0,lis)
        helper(arr,1,0,[0 for x in range(n)])


    return
func34()