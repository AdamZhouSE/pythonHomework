import math

s=list(input())
s.sort(key=lambda x:s.count(x),reverse=True)
a=math.ceil(len(s)/2)
l1=s[:a]
l2=s[a:]
if s.count(s[0])>a:
    print("")
else:
    print("".join([l1.pop(0) if i%2==0 else l2.pop(0) for i in range(len(s))]))