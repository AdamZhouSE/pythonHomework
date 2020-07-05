n=int(input())
res=''
for i in range(n):
    res=res+chr(ord('A')+i)+res
    
print(res)