s1=input()
s2=input()
for item in s2:
    if not item in s1:
        s2=s2.replace(item,"")
print(s1==s2)