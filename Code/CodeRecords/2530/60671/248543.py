strs=input()
strt=input()
strfin=""
for c in strt:
    if not (c in strs):
        strfin=strfin+c
strfin=strt+strfin
print(strs)