n=int(input())
s='A'
for i in range(1,n):
    temp=chr(ord('A')+i)
    s=s+temp+s
print(s)