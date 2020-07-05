def solution():
    inp=input().split()
    m=int(inp[0])
    n=int(inp[1])
    nums=input().split()
    arr=[]
    place=-1
    i=0
    while i<n and i < m:
        for j in range(n-i):
            if i%2==0:
                place+=1
            else:
                place+=-1
            arr.append(nums[place])
        i+=1
        for j in range(m-i):
            if i%2==1:
                place+=n
            else:
                place+=-n
            arr.append(nums[place])       
    result=''
    for i in range(len(arr)):
        result=result+arr[i]+' '
    print(result)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

