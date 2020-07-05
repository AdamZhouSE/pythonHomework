import re
string=input()
pattern=re.compile("(25)+")

print(len(pattern.findall(string)))
print(string)