
def func25():
    for _ in range(0,eval(input())):
        arr = list(map(int, input().split()))
        #print(arr)
        l,r,ans=arr[0],arr[1],0
        for i in range(l,r+1):
            if i//10==0 or i%11==0:
                ans+=1
        print(ans)

func25()