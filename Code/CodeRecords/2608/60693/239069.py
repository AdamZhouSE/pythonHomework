cases=int(input())
vowels=['a','e','i','o','u']
for x in range(cases):
    str=input()
    voindex=[]
    res=[]
    for i in range(len(str)):
        if str[i] in vowels:
            voindex.append(i)
    for x in voindex:
        tmp=[]
        tmp.append(str[x])
        start=x
        for j in range(start+1,len(str)):
            tmp.append(str[j])
            if j not in voindex:
                res.append(''.join(tmp))
    if res:
        print(' '.join(res))
    else:
        print('-1')