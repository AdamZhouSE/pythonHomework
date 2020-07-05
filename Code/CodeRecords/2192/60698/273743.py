def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=[]
        arr.append(n)
        app(arr,n,n,False)
        res=' '.join(list(map(str,arr)))+' '
        print(res)

def app(arr,n,target,re):
    if n>0 and not re:
        arr.append(n-5)
        if n-5==target:
            return
        else:
            app(arr,n-5,target,re)
    else:
        re=True
        arr.append(n+5)
        if n+5==target:
            return
        else:
            app(arr,n+5,target,re)
test()