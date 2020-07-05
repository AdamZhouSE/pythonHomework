s=input()
subs=input()
while s.__contains__(subs):
    s=s.replace(subs,'')
print(s,end='')