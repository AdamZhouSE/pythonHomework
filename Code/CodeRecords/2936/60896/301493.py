a=eval(input())
dict1={'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5','M':'6','N':'6','O':'6','P':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9','X':'9','Y':'9'}
record=[]
dict2={}
for i in range(a):
    res=''
    temp=input().split('-')
    s=''.join(temp)
    for i in range(len(s)):
        ch=s[i]
        if(ch.isdigit()):
            res+=ch
        else:
            res+=dict1[ch]
    if(res in record):
        if(res in dict2):
            dict2[res]+=1
        else: dict2[res]=2
    else:
        record.append(res)
if dict2=={}:
    print('No duplicates.',end='')
else:
    for i in dict2:
        t=i[0:3]+'-'+i[3:]
        print(t,end=' ')
        print(dict2[i])
            