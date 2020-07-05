import sys  
def f(s):
    a=[]
    for i in list(s):
        if i!='-':
            a.append(i)
    for i in range(len(a)):
        if not '9'>=a[i]>='0':
            a[i]=str(int((ord(a[i])-64)/2)+1)
    return ''.join(a)


a=int(input().strip())
t=[]
m=[]
for i in range(a):
    s=input().strip()
    t.append(s)
    m.append(f(s))
for i in range(len(m)):
    if m.count(m[i])>=2:
        print(m[i][0:3]+'-'+m[i][3:]+" "+str(m.count(m[i])))
        sys.exit(0)
print('No duplicates.',end='')