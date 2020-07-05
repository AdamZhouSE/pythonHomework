k = int(input())
n = 10**k
m = n*10
num = 1
time = 0
for i in range(1,1000):
    if(num%m==0):
        break
    if(num%n==0):
        time+=1
    num = num*i
print(time)