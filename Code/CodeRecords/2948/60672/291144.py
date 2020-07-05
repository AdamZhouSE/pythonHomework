def f(string):
    string=string
    nestring=list()
    for j in range(len(string)-1):
        nestring.append('a')
    for i in range(1,len(string)):
        minum=int(string[-i])+int(string[-i-1])
        if minum>=10:
            nestring[-i]=str(minum-10)
        else:
            nestring[-i]=str(minum)
    final=''
    for i in range(len(nestring)):
        final+=nestring[i]
    return final

abbre=str(input())
ST=int(input())
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(abbre)
print(ST)
nums={}
for i in range(26):
    nums[alpha[i]]=str(ST+i)
numstring=''
for v in abbre.upper():
    numstring+=nums[v]

while len(numstring)>2:
    numstring=f(numstring)
    if numstring=='100':
        break

print(numstring)