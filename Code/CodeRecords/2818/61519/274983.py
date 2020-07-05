word=list(input().split(" "))
num=list(input().split(" "))
num.sort()
time=int(word[1])
n=time*int(num[0])
for i in range(1,len(num)):
    n=n+int(num[i])*(time-1)
print(n)