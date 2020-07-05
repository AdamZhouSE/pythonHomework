def least(s,t):
    answer=''
    s=list(s)
    t=list(t)
    answers=[]
    midlist=[]
    for i in range(len(s)-len(t)):
        tt=[t[i] for i in range(len(t))]
        if s[i] not in set(t):
            continue
        else:
            for j in range(i,len(s)):
                if s[j] in tt:
                    tt.remove(s[j])
                    midlist.append(s[j])
                elif s[j] not in tt:
                    if tt==[]:
                        break
                    else:
                        midlist.append(s[j])
                elif tt==[]:
                    break
            answers.append(midlist)
            midlist=[]
    l=len(answers[0])
    index=0
    for i in range(len(answers)):
        if len(answers[i])<l:
            l=len(answers[i])
            index=i
    for i in range(len(answers[index])):
        answer=answer+answers[index][i]
    return answer
s=input()
t=input()
answer=least(s,t)
print(answer)