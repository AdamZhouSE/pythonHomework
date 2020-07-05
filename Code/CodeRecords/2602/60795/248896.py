arr1=input()
newarr1=""
arr2=input()
newarr2=""
for i in range(1,len(arr1)-1):
    newarr1=newarr1+arr1[i]
A=[int(n) for n in newarr1.split(',')]
for i in range(1,len(arr2)-1):
    newarr2=newarr2+arr2[i]
B=[int(n) for n in newarr2.split(',')]
max,num,apos,bpos=0,0,-1,-1
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if A[i]==B[j]:
            apos,bpos=i,j
            num=num+1
            p=True
            while p:
               if apos+1<len(A) and bpos+1<len(B):
                   bpos=bpos+1
                   apos=apos+1
               else:
                   if max<num:
                       max=num
                   p=False
                   num=0
               if A[apos]==B[bpos]:
                   num=num+1
               else:
                   if max<num:
                       max=num
                   num=0
                   p=False
print(max)