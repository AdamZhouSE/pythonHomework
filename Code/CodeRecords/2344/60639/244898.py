def solution():
    n=int(input())
    inp=input().split()
    d=int(input())
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    newnums=''
    for i in range(d,n):
        newnums=newnums+str(nums[i])+' '
    for i in range(d):
        newnums=newnums+str(nums[i])+' '
    print(newnums)

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

