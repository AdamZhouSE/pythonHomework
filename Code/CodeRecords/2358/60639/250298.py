def solution():
    inp=input().split()
    n=int(inp[0])
    k=int(inp[1])
    inp=input().split()
    arr=[]
    for i in range(n):
        arr.append(int(inp[i]))
    arr.sort()
    result=''
    for i in range(1,k+1):
        result+=str(arr[n-i])+' '
    print(result)



def main():
    T=int(input())
    for i in range(T):
        solution()

main()

