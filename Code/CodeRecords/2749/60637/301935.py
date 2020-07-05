n=(int)(input())
fathers=list(map(int,input().split(' ')))
fathers.insert(0,0)
s=input()
strings=['']*n
strings[0]=s[0]
def construct_str(i):
    global fathers,s,strings
    if(strings[i]==''):
        strings[i]=s[i]+construct_str(fathers[i]-1)
    return strings[i]
def cmp(str1,str2):
    if(str1==str2):
        return 0
    else:
        if(sorted([str1,str2])[0]==str1):
            return 1
        else:
            return -1

for i in range(n):
    construct_str(i)
result=[1]
for i in range(1,n):
    for j in range(len(result)):
        if(cmp(strings[i],strings[result[j]-1])==1):
            result.insert(j,i+1)
            break
        if(cmp(strings[i],strings[result[j]-1])==0):
            if(result.index(fathers[i])<result.index(fathers[result[j]-1])):
                result.insert(j,i+1)
                break
            if(result.index(fathers[i])==result.index(fathers[result[j]-1])):
                if(i<result[j]):
                    result.insert(j,i+1)
                    break
        if(j==len(result)-1):
            result.append(i+1)
for i in result:
    print(i,end=' ')
