def findStr(string,tmp,tmp_idx,idx,res,vowels):
    if tmp[0] in vowels and tmp[tmp_idx-1] not in vowels and ''.join(tmp[:tmp_idx]) not in res and tmp_idx>1:
        res.append(''.join(tmp[:tmp_idx]))
    if idx>=len(string):
        return
    tmp[tmp_idx]=string[idx]
    findStr(string,tmp,tmp_idx+1,idx+1,res,vowels)
    findStr(string,tmp,tmp_idx,idx+1,res,vowels)


cases=int(input())
vowels=['a','e','i','o','u']
for x in range(cases):
    string=input()
    res=[]
    voindex=[]
    for i in range(len(string)):
        if string[i] in vowels:
            voindex.append(i)

    for i in voindex:
        tmp = [0 for _ in range(len(string)-i)]
        findStr(string,tmp,0,i,res,vowels)
    res.sort()
    if not len(res):
        print(-1)
    for i in range(len(res)):
        print(res[i],end=' ' if i<len(res)-1 else '\n')