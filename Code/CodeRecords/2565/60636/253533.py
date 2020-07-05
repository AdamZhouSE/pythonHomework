nums1=eval(input())
nums2=eval(input())
num=[]
for i in nums1:
    num.append(i)
for i in nums2:
    num.append(i)
num.sort()
print("{:3f}".format((num[int(len(num)/2)]+num[int((len(num)-1)/2)])/2))