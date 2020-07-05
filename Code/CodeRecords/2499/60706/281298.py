n=int(input())
op=[]
for i in range(n):
    str1=input().split(' ')
    str2=''
    if str1[0]=='Add':
        str2=str1[1]+' '+str1[2]+' '+str1[3]
        op.append(str2)
    elif str1[0]=='Del':
        op[int(str1[1])-1]='0 0 0'
    elif str1[0]=='Query':
        case=int(str1[1])
        count=0
        for i in range(len(op)):
            list1=op[i].split(' ')
            if int(list1[0])*case+int(list1[1])>int(list1[2]):
                count=count+1            
        print(count)
            
        
    