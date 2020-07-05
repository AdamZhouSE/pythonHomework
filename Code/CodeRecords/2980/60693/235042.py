stroped=input()
op=input().split()
strout=''
strexist=0
if op[0]=='D':
    #delete operation
    for s in stroped:
        if(s==op[1]):
            strout=stroped.replace(s,'',1)
            strexist=1
            break#only delete the first one
if op[0]=='I':
    stroped_list=list(stroped)
    strindex=0
    count=0
    for s in stroped:
        count+=1
        if(s==op[1]):
            strindex=count
            strexist=1#no break, to get the last one
    stroped_list.insert(strindex-1,op[2])
    strout=''.join(stroped_list)
if op[0]=='R':
    #replace a character
    for s in stroped:
        if(s==op[1]):
            strout=stroped.replace(s,op[2])
            strexist=1
            break#operation already done
if strexist==0:
    print('no exist')
    print(stroped,end='')
print(strout)