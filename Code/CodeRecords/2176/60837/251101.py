def sort(string):
    List=[]
    result=[]
    for i in range(len(string)):
        List.append(ord(string[i]))
    for i in range(len(string)):
        thisPos=0
        thisChar='z'
        for j in range(len(List)):            
            if ord(thisChar)>=List[j]:
                thisChar=chr(List[j])
                thisPos=j+1
        List[thisPos-1]=ord('z')+1
        result.append(str(thisPos))
    return " ".join(result)

s=input()
print(sort(s))