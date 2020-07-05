import re
inp=input()
inp=re.findall("\"+\w+\"",inp)
a1=[]
a2=[]
for i in range(1,len(inp[0])-1):
    a1.append(inp[0][i])
for i in range(1,len(inp[1])-1):
    a2.append(inp[1][i])
if sorted(a1)==sorted(a2):
    print('true')
else:
    print('false')