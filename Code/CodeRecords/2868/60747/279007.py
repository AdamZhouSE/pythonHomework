n=int(input())
num=input().split(" ")
odd=0
even=0
for i in range(len(num)):
    num[i]=int(num[i])
    if num[i]%2==0:
        even+=1
    else:
        odd+=1
print(min(odd,even))

