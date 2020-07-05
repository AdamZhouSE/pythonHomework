def reverse(nums,k,n):
    newnums=''
    if k>=n:
        for i in range(n):
            newnums+=str(nums[n-1-i])+' '
        return(newnums)
    else:
        num=n
        times=1
        while num>=k:
            pro=k*times
            for i in range(k):
                newnums+=str(nums[pro-1-i])+' '
            num=num-k
            times=times+1
        if num>0:
            for i in range(num):
                newnums += str(nums[n - 1 - i]) + ' '
            return (newnums)
        else:
            return(newnums)


def solution():
    inp=input().split(' ')
    n=int(inp[0])
    k=int(inp[1])
    inp=input().split(' ')
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    print(reverse(nums,k,n))

def main():
    T=int(input())
    for i in range(T):
        solution()

main()

