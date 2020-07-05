res=[]

aaa=input()
print(a)
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
print(l)
l= list(map(int, l))

res+=l

aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
l= list(map(int, l))

res+=l

res.sort()

print(res)