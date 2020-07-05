time = int(input())
while(time>0):
    a = input()
    m = int(a[0])
    n = int(a[2])
    str1 = input()
    str1 = str1.split(" ")
    str2 = input()
    str2 = str2.split(" ")
    nums1 = []
    nums2 = []
    for i in range(0, m):
        nums1.append(int(str1[i]))
    for i in range(0, n):
        nums2.append(int(str2[i]))
    for i in range(0,n):
        for j in range(0,m):
            if(nums1[j]==nums2[i]):
                nums1[j] = -1
                nums2[i] = -1
                break
    judge = False
    for i in nums2:
        if(i!=-1):
            judge = True
    if(judge):
        print("No")
    else:
        print("Yes")
    time -= 1