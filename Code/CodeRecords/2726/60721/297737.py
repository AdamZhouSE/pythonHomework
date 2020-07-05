s=input()
s=s[1:len(s)-1]
s=s.split(",")
ind=s.index("null")
print(int(ind/2+1))