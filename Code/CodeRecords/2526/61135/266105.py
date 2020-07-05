import sys
input=sys.stdin.readlines()
list1=input[0]
list2=input[1]
a1=list1.replace('[','')
b1=a1.replace(']','')
c1=b1.replace('\n','')
d1=c1.split(',')
while 'null' in d1:
    d1.remove('null')
while '' in d1:
    d1.remove('')
e=list()
for x in range(0,len(d1)):
    e.append(int(d1[x]))
a2=list2.replace('[','')
b2=a2.replace(']','')
c2=b2.replace('\n','')
d2=c2.split(',')
while 'null' in d2:
    d2.remove('null')
while '' in d2:
    d2.remove('')
for y in range(0,len(d2)):
    e.append(int(d2[y]))
e.sort()
print(e)