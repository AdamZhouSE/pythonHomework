import re,sys
rp=input()
while True:
    line = sys.stdin.readline()
    if not line:
        break
    line=re.sub(rp,'',line,flags=re.IGNORECASE)
    line=re.sub(' ','',line,flags=re.IGNORECASE)
    print(line,end='')
print()