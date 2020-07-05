
def main():
    n=int(input())
    arr=list(map(int, input().split()))
    x=int(input())
    judge=0
    for i in range(len(arr)-3):
        for j in range(i+1,len(arr)-2):
            for k in range(j+1,len(arr)-1):
                for l in range(k+1,len(arr)):
                    if arr[i]+arr[j]+arr[k]+arr[l]==x:
                        judge=1
                    else:
                        continue
    print(judge)



T=int(input())
for i in range(T):
    main()


