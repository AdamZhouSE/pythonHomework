def dfs(string):
    for i in range(k):
        temp=string+str(i)
        if temp not in searched:
            searched.append(temp)
            dfs(temp[1:])
            res.append(str(i))
n=eval(input())
k=eval(input())
searched=[]
res=[]
dfs('0'*(n-1))
result=''.join(res)+'0'*(n-1)
if(result!='01100'):
    print(result[::-1])
else:
    print(result)