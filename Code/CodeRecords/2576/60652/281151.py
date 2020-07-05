def changing_arr():
    arr=list(map(int,input().split(',')))
    target=int(input())
    if sum(arr)<=target:
        return max(arr)

    def averange(n,target):
        a=target//n
        if target-a*n<=n/2:
            return a
        else:
            return a+1
    n=averange(len(arr),target)
    while n>min(arr):
        SUM=0
        for i in arr:
            if i<n:
                SUM+=i
                arr.pop(arr.index(i))
        n=averange(len(arr),target-SUM)
        target-=SUM
    return n


print(changing_arr())