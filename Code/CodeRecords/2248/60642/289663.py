n = int(input())
a = int(input())
b = int(input())
count = 0
for i in range(1,1000000007):
    if(i%a==0 or i%b==0):count+=1
    if(count==n):break
print(i%1000000007)