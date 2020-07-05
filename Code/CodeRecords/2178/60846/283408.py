input()
nums=[x for x in input().split()]
magicWords=set()
cnt=0
str=[]
for num in nums:
    if num not in magicWords:
        magicWords.add(num)
        cnt+=1
    for i in range(len(str)):
        tmp=""
        for j in range(i,len(str)):
            tmp+=str[j]
        tmp+=num
        if tmp not in magicWords:
            magicWords.add(tmp)
            cnt+=1
    str.append(num)
    print(cnt)
