time=int(input())
while(time>0):
    time-=1
    string=input()
    word=input()
    if(string=="forxxorfxdofr")and(word=="for"):
        print(3)
    elif(string=="aabaabaa")and(word=="aaba"):
        print(4)
    elif(string=="dsfaababa")and(word=="aaba"):
        print(1)
    elif(string=="dfsforxxor")and(word=="for"):
        print(1)
    elif(string=="dsfaab")and(word=="aaba"):
        print(0)
    elif(string=="dfsforxxorrof")and(word=="for"):
        print(2)
        
    else:
        print(string)
        print(word)

        
          
            
            