def solution():
    inp=input().split()
    n=int(inp[0])
    m=int(inp[1])
    x=int(inp[2])
    inp=input().split()
    arr1=[]
    for i in range(n):
        arr1.append(int(inp[i]))
    inp=input().split()
    arr2=[]
    for i in range(m):
        arr2.append(int(inp[i]))
    judge=0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]+arr2[j]==x:
                judge=1
                print(str(arr1[i])+' '+str(arr2[j]))
            else:
                continue
    if judge==0:
        print(-1)


def main():
    T=int(input())
    for i in range(T):
        solution()

main()

