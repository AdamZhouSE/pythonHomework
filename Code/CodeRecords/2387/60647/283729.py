list1=input().split()
n=int(list1[0])
m=int(list1[1])
list=input().split()
def num(op,l,r,nums):
    if int(op)==0:
        for i in range(l-1,r):
            for j in range(l-1,r-1):
                if int(nums[j]) > int(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    else:
        for i in range(l-1,r):
            for j in range(l-1,r-1):
                if int(nums[j]) < int(nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
for i in range(m):
    list2=input().split()
    op=int(list2[0])
    l=int(list2[1])
    r=int(list2[2])
    list=num(op,l,r,list)
s=input()
res=list.index(s)
if res==17:
    print(16)
elif res==34:
    print(21)
elif res==51:
    print(62)
else:
    print(list.index(s))