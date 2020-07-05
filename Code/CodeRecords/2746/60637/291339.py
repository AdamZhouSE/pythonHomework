beginWord=input()
endWord=input()
dictionary=eval(input())
dictionary.append(beginWord)
words=len(dictionary)
relations=[[0]*words for i in range(words)]
def accessable(a,b):
    count=0
    for i in a:
        if(i not in b):
            count+=1
        if(count>1):
            return False
    return True
routes=[]
def search(record,relation,target,word,length):
    global relations,routes
    if(word==target and length not in routes):
        routes.append(length)
    else:
        for i in range(len(relation)):
            if(relation[i]==1 and dictionary[i] not in record):
                record.append(dictionary[i])
                search(list.copy(record),relations[i],target,dictionary[i],length+1)
                record=record[:-1]
for i in range(len(dictionary)):
    for j in range(len(dictionary)):
        if(i!=j and accessable(dictionary[i],dictionary[j])):
            relations[i][j]=1
search([beginWord],relations[dictionary.index(beginWord)],endWord,beginWord,1)
if(routes==[]):
    print(0)
else:
    print(min(routes))

