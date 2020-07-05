words=input()
digits=[]
for word in words:
    init=int(0)#规范每个都是32的长度
    for i in range(len(word)):
        alp=word[i]
        temp=1<<(ord(alp)-ord('a'))#1左移相应位数  ord是char转成ASCII数字：97  chr是将ASCII转成char ：a
        init=init|temp#做或运算
    digits.append(init)

maxLen=0
for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        if digits[i]&digits[j]==0:
            temp=len(words[i])*len(words[j])
            maxLen=max(maxLen,temp)
print(maxLen)