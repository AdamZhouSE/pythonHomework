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
k=int(nums1[0])
m=int(nums1[0])
A=input().spilt(" ")
A=[int(x) for x in A]
B=input().split(" ")
B=[int(x) for x in B]
A=bubblemin(A)
B=bubblemax(B)

selectA=A[:k]
selectB=B[:m]

if max(selectA)<min(selectB):
    print("YES")
else:
    print("NO")

