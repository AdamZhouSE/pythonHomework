n=int(input())
result=[]
while n>0:
    s=input()
    while len(s)>1:
        nums=0
        for i in range(len(s)):
            nums=nums+int(s[i])
        s=str(nums)
    result.append(s)
    n=n-1

for i in range(len(result)):
    print(result[i])
