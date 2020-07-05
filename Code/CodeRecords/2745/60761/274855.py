def findline(result,lines,dictionary,endword):
    beginword=lines[-1]
    if(beginword==endword):
        result.append(lines)
    else:
        for word in dictionary:
            temp=dictionary[:]
            i=0
            for j in range(len(word)):
                if beginword[j]!=word[j]:
                    i+=1
            if(i==1):
                temp.remove(word)
                findline(result,lines+[word],temp[:],endword)
                
beginword=input()
endword=input()
dictionary=list(map(str,input()[2:-2].split('","')))
if(endword not in dictionary):
    print("[]")
else:
    result=[]
    length=1000
    lines=[beginword]
    dictionary.remove(biginword)
    findeline(result,lines,dictionary[:],endword)
    for line in result:
        length=min(length,len(line))
    for line in result:
        if(len(line)==length):
            print(line)