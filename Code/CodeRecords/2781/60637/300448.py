i=1
def infix(str1,str2):
    judge=True
    for i in range(len(str1)):
        if(str1[i]!=str2[i]):
            judge=False
            break
    return judge
while(True):
    temp=input()
    string=[]
    while(temp!='9'):
        string.append(temp)
        temp=input()
    judge=False
    for j in range(len(string)):
        for k in range(j+1,len(string)):
            if(infix(string[j],string[k])):
                judge=True
                break
        if(judge):
            break
    if(judge):
        print('Set %d is not immediately decodable'%i)
    else:
        print('Set %d is immediately decodable'%i)
    i+=1