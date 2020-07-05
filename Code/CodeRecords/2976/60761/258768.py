import sys
shortstr=input()
lines=sys.stdin.readlines()
for line in lines:
    line=line.replace(" ","")
    line=line.replace(shortstr.lower(),"")
    line=line.replace(shortstr.upper(),"")
    line=line.strip()
    print(line)
