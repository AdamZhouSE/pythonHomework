import re
n=input()
s=input()
s=re.sub(' +', ' ', s)
s=s.split(" ")
s.sort(reverse=True)
print("%d"%int("".join(s)),end='')