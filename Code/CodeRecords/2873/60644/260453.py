length=input().split()
l1=int(length[0])
l2=int(length[1])
s=input().split()
p=input().split()
res=''
for i in range(0,l1):
    c=s[i]
    for j in range(0,len(p)):
        try:
            if c == p[j]:
                res = res + ' ' + c
        except:
            print(s,p,l1,l2)
        
print(res[1:])
