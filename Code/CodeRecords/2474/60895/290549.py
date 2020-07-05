t=int(input()) 
while t>0:
    t=t-1
    temp=''
    string=input()
    i=0
    valid=0
    while i<len(string):
        if string[i]=='(':
            if string[i+1]==')':
                valid=valid+2
                i=i+2
            else:
                temp=temp+'('
                i=i+1
        else:
            temp=temp+')'
            i=i+1
    count=0
    for j in range(0,len(temp)):
        stop=False
        if temp[j]=='(':
            count=count+1
        else:
            if count>0:
                right=temp[j:j+count]
                for item in right:
                    if item==')':
                        valid=valid+2
                    else:
                        stop=True
                        break
            else:
                stop=True
                break
        if stop==True:
            break
    print(valid)      
            