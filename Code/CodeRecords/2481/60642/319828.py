times = int(input())
for j in range(times):
    input()
    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]
    same = []
    for i in range(len(nums1)):
        if(nums2.count(nums1[i])>0 and same.count(nums1[i])==0):
            same.append(nums1[i])
    print(len(same))