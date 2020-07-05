def bubblemax(ls):#从大到小排序
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]<ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
def bubblemin(ls):#从小到大排序
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls

nums1=input().split(" ")
nums2=input().split(" ")
k=int(nums2[0])
m=int(nums2[0])
s1=input()
s2=input()
j=0
A=[]
B=[]
while s1.__contains__(" "):
    index=s1.index(" ")
    A.append(int(s1[:index]))
    s1=s1[index+1:]
A.append(int(s1))
while s2.__contains__(" "):
    index=s2.index(" ")
    B.append(int(s2[:index]))
    s2=s2[index+1:]
B.append(int(s2))
A=bubblemin(A)
B=bubblemax(B)

selectA=A[:k]
selectB=B[:m]

result=""
if max(selectA)<min(selectB):
    result="YES"
else:
    result="NO"

    
print(result)

