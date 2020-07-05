far1=input()
a1=[]
far2=input()
a2=[]
nums='0123456789'
sign='+-'
stri=''
for i in range(len(far1)):
    if far1[i] in nums or far1[i] in sign:
        stri=stri+far1[i]
        for j in range(i+1,len(far1)):
            if far1[j] in nums:
                stri=stri+far1[i]
            else:
                break
        if stri!='+'and stri!='-':
            a1.append(int(stri))
        stri=''
for i in range(len(far2)):
    if far2[i] in nums or far2[i] in sign:
        stri=stri+far2[i]
        for j in range(i+1,len(far2)):
            if far2[j] in nums:
                stri=stri+far2[i]
            else:
                break
        if stri!='+'and stri!='-':
            a1.append(int(stri))
        stri=''
ar=a1+a2
ar=sorted(ar)
print(ar)