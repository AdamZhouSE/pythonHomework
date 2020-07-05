s=list(input())
s.sort()
# print(s)
pow2=[]
for i in range(10):
    x=list(str(pow(2,i)))
    x.sort()
    pow2.append(x)
# print(pow2)
isX=False
for item in pow2:
    if item==s:
        isX=True
if isX:
    print("true")
else:
    print("false")
