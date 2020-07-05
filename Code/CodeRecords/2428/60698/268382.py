def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=input().split()
        arr=list(map(int,arr))
        odd=[]
        even=[]
        for i in range(0,len(arr)):
            if arr[i]%2==0:
                even.append(arr[i])
            else:
                odd.append(arr[i])
        odd.sort(reverse=True)
        even.sort()
        res=list(map(str,odd))+list(map(str,even))
        res=' '.join(res)+' '
        print(res)
test()

