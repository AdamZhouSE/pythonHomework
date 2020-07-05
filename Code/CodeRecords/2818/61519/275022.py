word=list(input().split(" "))
num=list(input().split(" "))
for i in range(len(num)):
    num[i]=int(num[i])
time=int(word[1])
num.sort()
n=time*int(num[0])
for i in range(1,len(num)):
    if time>1:
        time=time-1
    n=n+num[i]*(time)
print(n)