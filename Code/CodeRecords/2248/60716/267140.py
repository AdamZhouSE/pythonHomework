n = int(input())
a = int(input())
b = int(input())
index = 1 
num = 0
while num!=n:
    if index%a==0 or index%b==0:
        num+=1
    index+=1
k = index%(1000000007)
print(k)
