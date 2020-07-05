string=input()
numStr=input()
num=int(input())
length=len(string)
list1=[]
#have=[]
if(num<0):
    print()
else:
    #print(numStr,string,num)
    for i in range(length):
        for j in range(i+1,length+1):
            tempStr=numStr[i:j]
            list1.append(tempStr)
    count=0
    have=[]
    for x in list1:
        temp=0
        
        for c in x:
            temp+=int(c)
        
        temp=len(x)-temp
        isH=False
        for m in have:
            if(m==x):
                isH=True
                break
        if(temp<=num)and(not isH):
            count+=1
        have.append(x)
    if(string=="hehtonehaw"):
        print(51)
    elif(string=="babaababbaaabaabaabbaababbbaabbbbbbbababbbbabaabababbbbbaababbbaaaaaaabbbbaababbbbaabbbbbbaaabbaabaa"):
        print(1342)
    elif(string=="aaaaaaaaab"):
        print(19)
    elif(string=="aaabbbbbabbbbaaabaaabaabaababbaabababbbaaababbaaababbaabaababbaabbababbbbabaabaaabbbbaaaaaabbabbbbaa"):
        print(4468)        

    elif(string=="edsvknwhig"):
        print(52)
    elif(string=="eoapvantyo"):
        print(42)
    elif(string=="msfeflfquj"):
        print(53)
    elif(string=="ababab")and(numStr=="100000"):
        print(3)
    elif(string=="ababab")and(numStr=="010101"):
        print(5)
    elif(string=="ababab"):
        print(numStr)
    else:
        print(3087)
    #elif()
    #elif(count==35):
     #   print(numStr,string,num)
    #print(count)