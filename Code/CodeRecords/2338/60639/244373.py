def solution():
    inp=input().split(' ')
    n=int(inp[0])
    sum=int(inp[1])
    inp=input().split(' ')
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==sum:
                print("Yes")
                return
            else:
                continue
    print("No")


def main():
    T=int(input())
    for i in range(T):
        solution()

main()

