from math import log

s=input()
s=s[1:len(s)-1].split(",")
print(int(log(len(s),2)))
