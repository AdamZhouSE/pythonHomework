def cal_match(done,rest,word):
    for i in range(len(rest),0,-1):
        if done[len(done)-1-(len(word)-i):len(done)-1]+rest[0:i]==word:
            return i
    return 0

def f(done,rest,choices):
    if len(rest)==0:
        return 0
    elif len(done)==0:
        choices.sort(reverse=True,key=lambda x:(len(x)))
        flag=False
        index=-1
        for ele in choices:
            index+=1
            if ele==rest[:len(ele)]:
                flag=True
                done+=rest[:len(ele)]
                rest=rest[len(ele):]
                break
        if flag:
            choices.pop(index)
            if f(done,rest,choices)==-1:
                return -1
            else:
                return f(done,rest,choices)+1
        else:
            return -1
    else:
        max_match=0
        max_index=0
        for i in range(0,len(choices)):
            if cal_match(done,rest,choices[i])>=max_match:
                max_match=cal_match(done,rest,choices[i])
                max_index=i
        if max_match==0:
            return -1
        else:
            choices.pop(max_index)
            return f(done+rest[:max_match],rest[max_match:],choices)+1
a=int(input().strip())
s=input().strip()
t=[]
for i in range(a):
    t.append(input().strip())
print(f("",s,t))
                
        
    