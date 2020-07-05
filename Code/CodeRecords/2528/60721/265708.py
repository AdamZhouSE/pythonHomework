import re
lis=re.findall(r"[-]{0,1}[0-9]{1,}",input())
lis=[int(i) for i in lis]
lis.sort()
print(lis)