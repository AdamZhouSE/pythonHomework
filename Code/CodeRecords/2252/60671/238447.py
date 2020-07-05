time=int(input())
while(time>0):
    string=input()
    word=input()
    count=0
    flagStart=False
    flagProcess=False
    flagEnd=False
    lenStr=len(string)
    lenWord=len(word)
    place=0
    for x in range(lenStr):
        if(string[x]==word[0])and(not flagProcess):
            flagStart=True
            flagProcess=True
            place+=1
        elif(string[x]==word[lenWord-1])and(flagProcess):
            flagStart=False
            flagProcess=False
            count+=1
        elif(string[x]==word[place])and(flagProcess):
            place+=1
        elif(string[x]!=word[place])and(flagProcess):
            place=0
            flagProcess=False
            flagStart=False
    print(count)
    time-=1

        
          
            
            