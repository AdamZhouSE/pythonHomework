n=int(input())
passages=[]
for i in range(n):
    passage=[x for x in input().split()]
    wordset=set()
    for word in passage:
        wordset.add(word)
    passages.append(wordset)
m=int(input())
for i in range(m):
    newWord=input()
    #flag=0
    for j in range(n):
        if newWord in passages[j]:
            print(j+1,'',end='')
            # if flag==0:
            #     flag=1
            #     print(j+1,end='')
            # else:
            #     print('',j+1,end='')
    print()
