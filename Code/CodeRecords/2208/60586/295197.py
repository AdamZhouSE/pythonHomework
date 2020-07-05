def exam27():
    T=int(input())
    for t in range(T):
        n=int(input())
        t=input().split(" ")
        arr=[]
        out=[]
        out.append(-1)
        for item in t:
            arr.append(int(item))
        for i in range(1,n):
            for j in range(i):
                if arr[j]<arr[i] :
                    pre=arr[j]
            out.append(pre)
        for i in range(0,n-1):
            print(out[i],end=" ")
        print(out[n-1])
exam27()