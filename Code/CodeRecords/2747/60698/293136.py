#string 17
def test():
    beginWord=input()
    endWord=input()
    dictionary=list(eval(input()))
    if endWord not in dictionary:
        print([])
        return
    else:
        length=[len(dictionary)]
        res=[beginWord]
        ans=[]

        trans(beginWord,endWord,dictionary,length,res,ans)
        print(ans)


def trans(beginWord,endWord,dictionary,length,res,ans):
    if beginWord==endWord:
        res.append(endWord)
        if len(res)<length[0]:
            ans.clear()
            ans.append(res)
            length[0]=len(res)
        elif len(res)==length[0]:
            ans.append(res)
    else:
        copy_dictionary=list(dictionary)
        copy_res=list(res)
        for word in dictionary:
            if able(word,beginWord):
                copy_dictionary.remove(word)
                copy_res.append(word)
                trans(word,endWord,copy_dictionary,length,copy_res,ans)
                copy_dictionary.append(word)
                copy_res.remove(word)


def able(thisWord,targetWord):
    count=0
    for i in range(0,len(thisWord)):
        if thisWord[i]!=targetWord[i]:
            count=count+1
        if count>=2:
            return False
    return True
test()