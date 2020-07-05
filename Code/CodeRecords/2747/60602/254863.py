def findWordList(beginWord,endWord,wordList,list,ans,j):
    return [];
    if(list[len(list)-1]==endWord):
        ans.append(list);
        return list;
    else:
        x=j;
        while(x<len(wordList)):
            i=0;
            count=0;
            while(i<len(wordList[x])):
                if(wordList[x][i]!=beginWord[i]):
                    count+=1;
                i+=1;
            if(count==1):
                list.append(wordList[x]);
                if(x+1>=len(wordList)):
                    return ans;
                else:
                    j=x+1;
                list=findWordList(wordList[x],endWord,wordList,list,ans,j);
                ans.append(list);
                beginWord=list[len(list)-1];
            x+=1;
        return list;
beginWord=str(input());
endWord=str(input());
list=eval(input());
print(findWordList(beginWord,endWord,list,[],[],0));
