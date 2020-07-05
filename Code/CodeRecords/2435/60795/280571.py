def maxchar(list):
    max=list[0]
    for i in range(1,len(list)):
        if list[i]>max:
            max=list[i]
    return max

arr=[int(n) for n in input().split(' ')]
n,m=arr[0],arr[1]
word,list=[],[]
re=[]
for i in range(0,n):
    str=input()
    word.append(str.lower())
for i in range(0,m):
    arr=[int(n) for n in input().split(' ')]
    list.append(arr)
for i in range(0,m):
    begin,end=list[i][0]-1,list[i][1]-1
    if begin==end:
        re.append(word[begin])
    else:
        max=word[begin]
        maxc=maxchar(word[begin])
        for j in range(begin+1,end+1):
            if word[j]=="yyy":
                max="yyy"
                break
            a=maxchar(word[j])
            if a>=maxc:
                max=word[j]
                maxc=a
        
        re.append(max)
        
for i in range(0,len(re)):
    print(re[i])

