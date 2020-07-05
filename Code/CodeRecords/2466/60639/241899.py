def solution():
    n=int(input())
    nums=input().split(' ')
    for i in range(n):
        nums[i]=int(nums[i])
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                a=nums[i]
                b=nums[j]
                c=nums[k]
                if check(a,b,c)==1:
                    count=count+1
                else:
                    continue
    print(count)

def check(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        if abs(a-b)<c and abs(b-c)<a and abs(a-c)<b:
            return 1
        else:
            return 0
    else:
        return 0

def main():
    T=int(input())
    for i in range(T):
        solution()

main()
