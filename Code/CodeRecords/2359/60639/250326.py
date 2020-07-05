def solution():
    n=int(input())
    inp=input().split()
    arr=[]
    for i in range(n):
        arr.append(int(inp[i]))
    arr.sort()
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]==arr[k]:
                    count+=1
                else:
                    continue
    if count==0:
        print(-1)
    else:
        print(count)



def main():
    T=int(input())
    for i in range(T):
        solution()

main()

