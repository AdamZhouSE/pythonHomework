string=bin(int(input()))[2:]

res=0
used=0
i=0
while i<len(string):
    if string[i]=="1":
        res=max(i-used,res)
        used=i
    i=i+1
print(res)
