a = input()
a=a.replace('[','').replace(']','').split(',')
b=[]
for i in a:
    b.append(int(i))
b=sorted(b)
print(b)