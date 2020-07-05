beginword=input()
endword=input()
dictionary=list(map(str,input()[2:-2].split('","')))
change=[[] for value in range(len(endword)+3) ]
temp=[]
change[0].append(endword)
if(endword in dictionary):
    dictionary.remove(endword)
    k=0
    #print(dictionary,beginword,endword)
    while(dictionary):
        for word in dictionary:
            for eword in change[k]:
                i=0
                for j in range(len(word)):
                    if word[j]!=eword[j]:
                        i+=1
                if i==1:
                    change[k+1].append(word)
                    break
                elif(eword==change[k][-1]): 
                    temp.append(word)
        dictionary=temp[:]
        temp=[]
        k+=1
    #print(change,beginword,endword)
    m=0
    for i in range(0,len(change)):
        for word in change[i]:
            m=0
            for j in range(len(word)):
                if word[j]!=beginword[j]:
                    m+=1
            if m==1:
                print(i+2)
                break
        if(m==1):
            break
    if(m==0):
        print(0)
else:
    print(0)