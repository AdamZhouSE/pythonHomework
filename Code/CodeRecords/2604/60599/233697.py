s=input()
k=input()

s="".join(s.split(' '))
s="".join(s.split('"'))

l=list(s[1:len(s)-1].split(','))
l.sort()
for i in l:
    if(i>k):
        print(i)
        exit()
print(l[0])