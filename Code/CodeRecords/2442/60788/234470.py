from sys import stdin
s=stdin.readline()
t=s[1:len(s)-1]
h=t.split(',')
m=[int(x) for x in h]
m.sort(reverse=False)
if len(m)<2:
    print(0)
else:
    iterator=iter(m)
    first=next(iterator)
    second=next(iterator)
    max=int(second)-int(first)
    while True:
        first=second 
        second=next(iterator,'f')
        if second=='f':
             print(max)
        if int(second)-int(first)>max:
            max=int(second)-int(first)
   