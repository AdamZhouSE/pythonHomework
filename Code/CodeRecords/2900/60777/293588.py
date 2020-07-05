s=input()

res=0

for x in s:
    if(x.isalnum()):
        res+=1
        
print(res,end='')