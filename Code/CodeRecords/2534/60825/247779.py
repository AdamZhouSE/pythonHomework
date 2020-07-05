res=[]
s=input()
s=s[1:len(s)-1]
s=s.replace('[','')
s=s.replace(']','')
l=s.split(',')
l= list(map(int, l))
print(l)

l.sort()
print(l)
    