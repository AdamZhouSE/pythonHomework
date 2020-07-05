def pair():
    T=int(input())
    for i in range(0,T):
        find_Pair()

def find_Pair():
    N=int(input())
    arr=list(map(int, input().split(" ")))
    K=int(input())
    out=[]
    for i in range(0,len(arr)-1):
        if i in out:
            continue
        for j in range(i+1, len(arr)):
            if j in out:
                continue
            if arr[i]+arr[j]==K:
                out.append(i)
                out.append(j)
                print(str(arr[i]+" "+arr[j]+" "+str(K)))
    if not out:
        print("-1")
if __name__=='__main__':
    pair()