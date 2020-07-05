def delete(string,target):
    temp=list(string)
    exist=False
    for i in range(len(string)):
        if temp[i]==target:
            del temp[i]
            exist=True
            break
    if(exist):
        return "".join(temp)
    else:
        return "no exist"
def ins(string,target,char):
    temp=list(string)
    exist = False
    for i in range(len(string)-1,-1,-1):
        if temp[i]==target:
            temp.insert(i,char)
            exist = True
            break
    if (exist):
        return "".join(temp)
    else:
        return "no exist"
def rep(string,target,char):
    temp=list(string)
    if(target in temp):
        return string.replace(target,char)
    else:
        return  "no exist"
string=input()
instruction=input().split(' ')
result=''
if(instruction[0]=='D'):
    result=delete(string,instruction[2])
elif(instruction[0]=='I'):
    result=(ins(string,instruction[2],instruction[3]))
else:
    result=(rep(string,instruction[2],instruction[3]))
print(result)
if(result=='no exist'):
    print(string)