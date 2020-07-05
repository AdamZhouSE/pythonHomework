def intToBinary(n):
    str1=""
    while n>0:
        rem=n%2
        n=n//2
        str1=str(rem)+str1
    return str1

n=int(input())
str1=intToBinary(n)
count=0
for i in range(0,len(str1)):
    if str1[i]=="1":
        first=i
        for j in range(first+1,len(str1)):
            if str1[j]=='1':
                count1=j-first
                if count1>count:
                    count=count1
                break
print(count)
        