s=input()
subs=input()
while s.__contains__(subs):
    s=s.replace(subs,'')

if len(s)==0:
    s=subs    

print(s,end='')