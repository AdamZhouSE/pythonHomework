first_line=input().split(" ")
n=int(first_line[0])
x=int(first_line[1])
time = list(map(int,input().split(" ")))
time.sort()
res=0
for i in range(0,n):
    res+=time[i]*x
    if not x==1:
        x-=1
print(res)        