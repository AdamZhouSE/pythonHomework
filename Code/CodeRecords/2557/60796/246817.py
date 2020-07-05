n=int(input())
ls=[]
while n>0:
    ls.append(input())
    n=n-1
print(ls)

for i in range(len(ls)):
    s=ls[i]
    j=0
    while j<len(s)-1:
        k=j+1
        while k<len(s):
            if s[k]==s[k-1]:#删除s[k]
                if k==len(s)-1:
                    s=s[:k]
                else:
                    s=s[:k]+s[k+1:]
                k=k-1
            k=k+1
        j=j+1
        
        
for i in range(len(ls)):
    print(ls[i])
            
                
                