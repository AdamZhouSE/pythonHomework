
arr=list(map(int,input().split(",")))
size=len(arr)

f=[]
for k in range(0,size):
    num=0
    for i in range(0,size):
        num+=i*arr[-k+i]
    f.append(num)
print(max(f))