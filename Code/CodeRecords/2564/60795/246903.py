arr=raw_input()
newarr=""
for i in range(0,len(arr)-1):
    if i!=0:
        newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
k=int(input())
x=int(input())
num=[]
mark,left,right,min=-1,1,1,0
for i in range(0,len(list)):
   if list[i]==x:
      mark=i
      num.append(x)
      k=k-1
      break
if mark==-1:
   min=x-list[0]
   if min<0:
      min=0-min
   mark=0
   for i in range(0,len(list)):
      a=x-list[i]
      if a<0:
         a=0-a
      if a<min:
         min=a
         mark=i
   num.append(list[mark])
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