s=input()
i=0

while i<len(s)-2:
    if s[i]==",":
        i=i+1
    s=s[:i+1]+","+s[i+1:]
    i=i+1
ls=s.split(",")

for i in range(0,len(ls)-1):
    j=i+1
    while j<len(ls):
        if ord(ls[i])>ord(ls[j]):
            temp=ls[j]
            ls[j]=ls[i]
            ls[i]=temp
        j=j+1
            
print(''.join(ls))
    
    