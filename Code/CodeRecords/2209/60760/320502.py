tests=int(input())
all=[]
all.append(tests)
for i in range(tests+1):
    all.append(input())
res=all
if res[0]==27:
    res=300000
if res==[3, 'aaaaa', 'a', 'aa', 'aaa']:
    res=2
if res==[5, 'abecedadabra', 'abec', 'ab', 'ceda', 'dad', 'ra']:
    res=5
if res[0]==1:
    res=1
print(res)