s=input()
s=s[1:len(s)-1]
a=s.split(",")
a.sort()
l=list(map(int,a))
print(l)