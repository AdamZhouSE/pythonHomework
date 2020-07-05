n = int(input())
for i in range(n):
    s=input()
    nums=list(map(int,input().split()))
    nums2=list(map(int,input().split()))
    set1=set(nums+nums2)
    print(len(set1))
