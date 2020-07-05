s=input()
subs=input()
while s.__contains__(subs):
    if len(s)<=len(subs):
        break
    s=s.replace(subs,'')
    
    
print(s,end='')