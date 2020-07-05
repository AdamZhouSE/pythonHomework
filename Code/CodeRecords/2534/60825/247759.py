res=[]
s=input()
s=s[1:len(s)-1]
s.replace('','[')
ss=s.split(",")
print(ss)

for a in ss:
    a=a[1:len(a)-1]
    print(a)
    #l=a.split(",")
    #l= list(map(int, l))
    #res+=l

res.sort()
print(res)
    