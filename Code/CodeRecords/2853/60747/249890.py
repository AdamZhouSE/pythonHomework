n=int(input())
odd=0
even=0
for i in range(n):
    num = input().split(" ")
for j in range(n):
    if num[j]%2==1:
        odd+=1
    else:
        even+=1
if odd%2==0:
    print(even)
else:
    print(odd)