l=int(input())
binstr=input()
count=0
for i in binstr:
    if i=="0":
        count=count+1
print("1"+count*"0",end="")