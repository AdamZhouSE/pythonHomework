a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
num = 0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]*2:
            num+=1
print(num)
