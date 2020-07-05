s=input()
i=0

while i<len(s)-2:
    if s[i]==",":
        i=i+1
    s=s[:i+1]+","+s[i+1:]
    i=i+1
ls=s.split(",")

for i in range(0,len(ls)):
    
    