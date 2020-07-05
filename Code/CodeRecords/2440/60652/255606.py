l=input().replace('[','').replace(']','')
s=list(map(int,l.split(',')))
s.sort()
print(s)