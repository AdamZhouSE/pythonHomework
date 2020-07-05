firstLine=input()
n=int(firstLine)
secondLine=input().split()
one2h=0
n2h=0
for i in range(n):
    if int(secondLine[i])==1:
        one2h=i
    elif int(secondLine[i])==n:
        n2h=i
print(max(max(max(one2h,n2h),n-1-one2h),n-1-n2h))