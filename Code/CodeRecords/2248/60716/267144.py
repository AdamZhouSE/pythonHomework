n = int(input())
a = int(input())
b = int(input())
index = 0 
num = 0
while num!=n:
    index+=1
    if index%a==0 or index%b==0:
        num+=1
k = index%(1000000007)
print(k)
