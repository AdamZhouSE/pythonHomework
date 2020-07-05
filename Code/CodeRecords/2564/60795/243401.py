arr=input()
list=[int(n) for n in arr.split(',')]
k=int(input())
x=int(input())
num=[]
mark,left,right=0,1,1
for i in list:
   if list[i]==x:
      mark=i
      num.append(x)
      break
k=k-1
while k>0:
   le=ri=-1
   if mark-left>=0:
      le=x-list[mark-left]
   if (mark+right)<len(list):
      ri=list[mark+right]-x
   if le>=0 and ri>=0:
      if le<=ri:
         num.insert(0,list[mark-left])
         left=left+1
      else:
         num.append(list[mark+right])
         right=right+1
   elif le==-1 and ri>=0:
      num.append(list[mark + right])
      right = right + 1
   elif le>=0 and ri==-1:
      num.insert(0,list[mark - left])
      left = left + 1
   k=k-1
for i in range(0, k):
    num[i] = int(num[i])
for m in range(0,k):
   for n in range(i+1,k):
      if num[m]>num[n]:
         num[m],num[n]=num[n],num[m]
print(num)