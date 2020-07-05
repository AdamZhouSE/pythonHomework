s=''
n=int(input())
for i in range(n):
    s=s+chr(ord('A')+i)+s
    
print(s)