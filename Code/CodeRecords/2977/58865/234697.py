#构建翻译字典
a='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
revA=''.join(reversed(a))
revB=''.join(reversed(b))
dicA=dict(zip(a,revA))
dicB=dict(zip(b,revB))


#获取输入
inputs=[]
while 1:
    s=input()
    if(s=='!'):
        break
    inputs.append(s)
    

s=[list(k) for k in inputs]

for j in s:
    for i in range(len(j)):
        if j[i] in a:
            j[i]=dicA.get(j[i])
        elif j[i] in b:
            j[i]=dicB.get(j[i])
    print(''.join(j))