arr1=input().split(",")
arr2=input().split(",")
sum1=0
sum2=0
i=len(arr1)-1
while i>=0:
    if arr1[i]=='1':
        sum1=sum1+pow(-2,len(arr1)-1-i)
    i=i-1
j=len(arr2)-1
while j>=0:
    if arr2[j]=='1':
        sum2=sum2+pow(-2,len(arr2)-1-j)
    j=j-1
N=sum1+sum2
if N == 0:

            digits = ['0']
else:

            digits = []

            while N != 0:

                N, remainder = divmod(N, -2)

                if remainder < 0:

                    N, remainder = N + 1, remainder + 2

                digits.append(str(remainder))
s="".join(digits[::-1])
result=[]
for k in s:
    result.append(int(k))
print(result)