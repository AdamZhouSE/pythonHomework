import copy
def compstr(str1,str2):
    count=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    if count==1:
        return True
    else:
        return False
    
beginword=input() #起始单词
endword=input()   #结束单词
wordlist=eval(input())  #单词表
templist=[]
for i in range(len(wordlist)):
    templist.append([])
for i in range(len(wordlist)):
    for j in range(len(wordlist)):
        if compstr(wordlist[i],wordlist[j]):
            templist[i].append(j)

final=[]
jix=[]
def jutou(i):
    final.append(i)
    for each in templist[i]:
        if wordlist[each]==endword:
            final.append(each)
            juba=copy.deepcopy(final)
            jix.append(juba)
            final.remove(each)
        elif each not in final:
            jutou(each)
        else:
            continue
    final.remove(i)
lix=[]
for i in range(len(wordlist)):
    jix=[]
    if compstr(beginword,wordlist[i]):
        jutou(i)
    lix+=jix
for each in lix:
    for eeach in lix:
        if len(eeach)>len(each):
            lix.remove(eeach)
b=[]
for each in lix:
    mystr=''
    for eeach in each:
        mystr+='.'+wordlist[eeach]
    a=mystr.split('.')
    a[0]=beginword
    b.append(a)
print(b)