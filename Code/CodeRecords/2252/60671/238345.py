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
        if(string[x]==word[0])and(!flagProcess):
            flagStart=True
            flagProcess=True
            
            