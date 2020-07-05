try:
    a=input().lstrip("[").rstrip("]").split(",")
    b=input().lstrip("[").rstrip("]").split(",")

except BaseException:
    print(a)
    print(b)
c=[]
for i in a:
    if i!="null" and i!="":
        c.append(int(i))
for i in b:
    if i!="null" and i!="":
        c.append(int(i))
c.sort()
print(c)