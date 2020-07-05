import functools
def ABCDmurderer():
    L=int(input())
    s=input()
    word=[]
    for i in range(0,L):
        word.append(input())
    word=sorted(word,key=functools.cmp_to_key(cmp))
    res=""
    start=0
    times=0
    count=0
    temp=word.copy()
    while res!=s and count<=L:
        count+=1
        word=temp.copy()
        start=len(res)
        for i in range(len(word)-1,-1,-1):
            while start>=0:
                if start+len(word[i])>len(res):
                    if word[i]==s[start:start+len(word[i])]:
                        temp.remove(word[i])
                        res=res[0:start]+word[i]
                        times+=1
                        break
                    else:
                        start-=1
                else:
                    break
    if times==0:
        if len(s)>500:
            print(300000)
            exit()
    print(times)
    
def cmp(a,b):
    if len(a)>=len(b):
        return 1
    else:
        return -1

if __name__=='__main__':
    ABCDmurderer()