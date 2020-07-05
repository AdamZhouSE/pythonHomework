num=int(input())
str=bin(num)
maxn=0
begin=0
end=0
for i in range(2,len(str)):
    if str[i]=="1":
        end=i
        if begin==0:
            maxn=0
        else:
            maxn=max(maxn,end-begin)
        begin=i
print(maxn)