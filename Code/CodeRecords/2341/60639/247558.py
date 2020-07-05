def solution():
    inp=input().split()
    n=int(inp[0])
    m=int(inp[1])
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr=arr1+arr2
    arr.sort()
    result=''
    for i in range(m+n):
        result=result+str(arr[i])+' '
    print(result)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

