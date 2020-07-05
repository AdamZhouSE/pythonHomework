s=input()
pairs=list(map(str,input()[2:-2].split("],[")))
print(s)
for pair in pairs:
    i,j=map(int,pair.split(","))
    if(ord(s[i])>ord(s[j])):
        s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
print(s,pairs)