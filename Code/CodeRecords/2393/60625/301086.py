test=int(input())
for i in range(test):
    len=input()
    numStr=input().split(' ')
    nums1=[]
    for c in numStr:
        nums1.append(int(c))

    numStr = input().split(' ')
    nums2 = []
    for c in numStr:
        nums2.append(int(c))

    count=0
    for x in nums1:
        for y in nums2:
            if x**y>y**x:
                count+=1
    print(count)