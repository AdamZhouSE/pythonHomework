str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
nums1=[]
for i in range(len(list1)):
    nums1.append(int(list1[i]))
str2=input()
str2=str2.replace('[','')
str2=str2.replace(']','')
list2=str2.split(',')
nums2=[]
for i in range(len(list2)):
    nums2.append(int(list2[i]))
nums1.extend(nums2)
nums1.sort()
length=len(nums1)
ans=0
if length%2==1:
    ans=nums1[length//2]
else:
    ans=(nums1[length//2]+nums1[length//2-1])/2.0
a_s=str(ans)
list3=a_s.split('.')
while len(list3[1])<5:
    list3[1]=list3[1]+'0'
ass=list3[0]+'.'+list3[1]
print(ass)