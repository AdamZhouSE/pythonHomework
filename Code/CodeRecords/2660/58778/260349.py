n=int(input())
temp=[]
for i in range(n):
    s=input()
    sl=s.split( )
    if(sl[0]=='T'):
        temp.append(sl[1])
    elif(sl[0]=='Q'):
        print(temp[int(sl[1])-1])
    else:
        temp=temp[0:len(temp)-int(sl[1])]