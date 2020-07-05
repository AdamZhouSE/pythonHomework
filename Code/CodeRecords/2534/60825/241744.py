res=[]
s=input()
s=s[1:len(s)-1]
s=s.split(",")

for a in s:
    a=a[1:len(a)-1]
    print(a)
    #l=a.split(",")
    #l= list(map(int, l))
    #res+=l

res.sort()
print(res)
    