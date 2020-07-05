nums=eval(input())
x=dict((a,L.count(a)) for a in nums)
y=[k for k,v in x.items() if max(x.values())==v]
print(y)