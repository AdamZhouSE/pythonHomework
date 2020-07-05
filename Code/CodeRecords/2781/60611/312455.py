import sys
c=0
while True:
    line = sys.stdin.readline().strip()
    if line=='':
        break
    l=[]
    
    while line!='9':
        l.append(line)
        line=input()
    l=sorted(l,key = lambda i:len(i))
    c+=1
    flag=False
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j][0:len(l[i])]:
                flag=True
                break
        if flag:
            break
    s="Set "
    s+=str(c)
    if flag:
        s += " is not immediately decodable"
        print(s)
    else:
        s += " is immediately decodable"
        print(s)