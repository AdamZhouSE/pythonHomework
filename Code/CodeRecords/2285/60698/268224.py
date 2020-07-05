#39
def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=input().split()
        arr=list(map(int,arr))
        result=[]
        i=0
        while i<len(arr)-1:
            for j in range(len(arr)-1,i,-1):
                if arr[i:j+1]==sorted(arr[i:j+1]):
                    result.append('('+str(i)+' '+str(j)+')')
                    i=j
                    break

            i=i+1
        res=' '.join(result)
        print(res)
test()

