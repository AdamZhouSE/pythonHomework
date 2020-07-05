a=input()
b=input()
count=0
if len(a)>len(b):
    count+=len(a)-len(b)
    for i in b:
        if not i in a:
            count+=1
if len(a)==len(b):
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            count+=1
if len(a)<len(b):
    count+=len(b)-len(a)
    for i in a:
        if not i in b:
            count+=1
print(count)