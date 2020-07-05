def makesubstring(st):
    answer=[st]
    if(len(st)!=2):
       temp=[]
       for i in range(1,len(st)-1):
           t=st[0:i]+st[i+1:len(st)]
           answer.append(t)
           if(len(t)>2):
               temp.append(t)
       while len(temp)!=0:
           t=[]
           for i in temp:
               for j in range(1,len(i)-1):
                   x=i[0:j]+i[j+1:len(i)]
                   answer.append(x)
                   if(len(x)>2):
                       t.append(x)
           temp=t
    return answer

def func(s):
    temp=[]
    for j in range(len(s)):
        if(s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u'):
            for k in range(j+1,len(s)):
                if(s[k]!='a' and s[k]!='e' and s[k]!='i' and s[k]!='o' and s[k]!='u'):
                    temp.append(s[j:k+1])
    if(len(temp)==0):
        print(-1)
    else:
        result = []
        for i in temp:
            result += makesubstring(i)
        set1 = set(result)
        fin = list(set1)
        fin.sort()
        for i in range(len(fin)):
            if (i == 0):
                print(fin[0], end='')
            else:
                print('', fin[i], end='')
        print('')


n=int(input())
for i in range(n):
    s=input()
    func(s)