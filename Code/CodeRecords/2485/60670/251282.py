t=int(input())
for i in range (0,t):
    n=int(input())
    words=input().split(' ')
    dic={}
    for j in range(0,n):
        word="".join(sorted(list(words[j])))
        #print(word)
        if word in dic:
            dic[word]=dic[word]+1
        else :
            dic[word]=1
    arr=sorted(dic.values())
    for k in range(0,len(arr)-1):
        print(arr[k],end=" ")
    print(arr[len(arr)-1])
        