n=int(input())
nums=input().split(" ")
NumOf2=0
NumOf1=0
for i in nums:
    if i=='1':
        NumOf1+=1
    else:
        NumOf2+=1
res=0
if NumOf2>=NumOf1:
    res=NumOf1
else:
    res=NumOf2+(NumOf1-NumOf2)//3

print(res)