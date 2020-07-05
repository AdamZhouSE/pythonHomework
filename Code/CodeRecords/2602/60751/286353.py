nums1=input().split(",")
nums1[0]=nums1[0][1:len(nums1[0])]
nums1[-1]=nums1[-1][0:-1]
nums2=input().split(",")
nums2[0]=nums2[0][1:len(nums2[0])]
nums2[-1]=nums2[-1][0:-1]
n1=len(nums1)
n2=len(nums2)
dp=[[0 for _ in range(n1+1)]for _ in range(n2+1)]
for i in range(1,n2+1):
    for j in range(1,n1+1):
        if nums1[j-1]==nums2[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
print(max(max(a) for a in dp))
