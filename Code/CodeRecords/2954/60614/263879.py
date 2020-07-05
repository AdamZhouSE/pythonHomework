num=int(input())
equation=[]
for i in range(num):
    equation.append(input())
possible=[]
for i in equation[0]:
    if equation[0].count(i)==1:
        possible.append(i)
n=0
while n<len(possible):
    for j in range(1,num):
        if equation[j].count(possible[n])!=1:
            del possible[n]
            n-=1
    n+=1
ans=[]
def guess(now,remaining,ans,store):
    judge=True
    for i in 'abcdefghijklm':
        if i in now:
            judge=False
            for j in remaining:
                if j=='+' or j=='*':
                    if now.index(i)==0 or now.index(i)==len(now)-1:
                        continue
                    if now[now.index(i)-1]=='+' or now[now.index(i)-1]=='*' or now[now.index(i)+1]=='+' or now[now.index(i)+1]=='*':
                        continue
                tempNow = now.replace(i,j)
                tempStore=[[i,j]]+store
                tempRemaining=remaining.replace(j,'')
                ans=guess(tempNow,tempRemaining,ans,tempStore)
            break
    if judge:
        try:
            if eval(now):
                ans.append(store)
        except:
            pass
    return ans
result=[]
for i in possible:
    tempEquation=equation[0].replace(i,"==")
    ans=guess(tempEquation,'0123456789+*',[],[])
    for j in range(1,len(equation)):
        newAns=[]
        for k in ans:
            tempEquation=equation[j].replace(i,"==")
            tempRemaining='0123456789+*'
            for l in k:
                tempEquation=tempEquation.replace(l[0],l[1])
                tempRemaining=tempRemaining.replace(l[1],'')
            judge=False
            for l in 'abcdefghijklm':
                if l in tempEquation:
                    judge=True
                    break
            if judge:
                tempAns=guess(tempEquation,tempRemaining,[],k)
                newAns+=tempAns
        ans=newAns
    for j in ans:
        j.append([i,'='])
        result.append(j)
output=[]
if len(result)>0:
    for i in result[0]:
        judge=True
        for j in result:
            if i not in j:
                judge=False
                break
        if judge:
           output.append(i)
    output.sort(key=lambda x:x[0])
    for i in output:
        print(i[0]+i[1])
else:
    print("noway")