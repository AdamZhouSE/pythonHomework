s=input()
subs=input()
while s.__contains__(subs):
    s=s.replace(subs,'')
    if len(s)<=len(subs):
        break
print(s,end='')