#39
def test():
    t=int(input())
    for _ in range(0,t):
        max_exp=0
        n=int(input())
        arr=input().split()
        arr=list(map(int,arr))
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    if max_exp<j-i:
                        max_exp=j-i
        print(max_exp)
test()

