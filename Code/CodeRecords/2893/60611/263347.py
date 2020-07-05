source=input()
l=source[1:-1].split(",")
s=set(l)
for i in s:
    if source.count(i)!=3:
        print(i)
        break