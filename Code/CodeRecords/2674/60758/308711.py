out=[]
def deep(current,index,temp,get):
    if current=='c':
        out.append(temp)
    for i in range(index,len(get)):
        if current=='*':
            if get[i]=='a':
                deep(get[i],i+1,temp+get[i],get)
        elif(current=='a'):
            if get[i]=='a' or get[i]=='b':
                deep(get[i],i+1,temp+get[i],get)
        elif(current=='b'):
            if get[i]=='b' or get[i]=='c':
                deep(get[i],i+1,temp+get[i],get)
        elif(current=='c'):
            if get[i]=='c':
                deep(get[i],i+1,temp+get[i],get)

for _ in range(int(input())):
    get=input()
    out=[]
    deep('*',0,"",get)
    print(len(out))
    