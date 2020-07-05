n=input()
res=''
if n=='0':
    print(str(0),end='')
else:
    for i in range(len(n)):
        res+=n[len(n)-i-1]
while res.startswith('0'):
    res=res[1:]
if res.endswith('-'):
    res='-'+res[:-1]
print(res)