l=eval(input())
l=sorted(l,key=lambda x:x[1],reverse=True)
e=set()
result='true'
for i in l:
    if i[1]=='=':
        e.add(i[0])
        e.add(i[3])
    else:
        if i[0] in e and i[3] in e:
            result='false'
            break
print(result)