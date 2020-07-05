def solution():
    n=int(input())
    inp=input().split()
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                count+=1
    print(count)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

