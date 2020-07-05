def zhaoBuTong(a,b):
    answer=0
    for i in range(str(a).__len__()):
        if a[i:i+1]!=b[i:i+1]:
            answer+=1
    return answer
answerList=[]


def recursion (begin,end,wordList,wordLength,answer):
    tem=[]
    if zhaoBuTong(end, answer[answer.__len__() - 1]) == 1:
        answerList.append(list(answer))
        return
    for i in range(wordLength):
        if zhaoBuTong(wordList[i],answer[answer.__len__()-1])==1 and wordList[i] not in answer:
            tem.append(wordList[i])
    for i in tem:
        answer.append(i)
        recursion(begin,end,wordList,wordLength,answer)
        answer.remove(i)

begin=input()
end=input()
string=input()[2:]
wordList=[]

i=0
while i<string.__len__():
    wordList.append(string[i:i+3])
    i+=6

for i in wordList:
    if i==end or i==begin:
        wordList.remove(i)
answer=[]
answer.append(begin)
recursion(begin,end,wordList,wordList.__len__(),answer)
if answerList.__len__()==0:
    print([])
elif end not in wordList:
    print([])
else:
    minlen=list(answerList[0]).__len__()
    for i in answerList:
        if list(i).__len__()<minlen:
            minlen=list(i).__len__()
    for i in answerList[::]:
        if list(i).__len__()>minlen:
            answerList.remove(list(i))
    result=[]
    for i in range(answerList.__len__()):
        tem=[]
        for j in answerList[i]:
            tem.append(j)
        tem.append(end)
        result.append(tem)
    print(result)