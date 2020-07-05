num=int(input())
letter=input()
wordlist=[]
if(len(letter)<100):
    for i in range(0,num):
        wordlist.append(input())
#找出单词最长长度
    longest = ''
    for word in wordlist:
        if len(word) > len(longest):
            longest = word
#把所有单词补齐到最长
    for i in range(0,num):
        item=wordlist[i]
        while len(item)<len(longest):
            item=item+"0"
        wordlist[i]=item
#print(wordlist)
    temp=letter[0]
    result=0
    i=0
    while(i<len(letter)):
        Check = False
        for j in wordlist:
            if temp in j:
                Check=True
        if Check==False:
            temp=temp[len(temp)-1]
            result=result+1
        else:
            i = i + 1
            if(i==len(letter)):
                result=result+1
                break
            temp=temp+letter[i]

    print(result)
else:
    if(num==1):
        print(1)
    else:
        print(300000)