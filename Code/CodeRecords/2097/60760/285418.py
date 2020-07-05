a=int(input())
b=int(input())
res=str(a/b)
if res.endswith('.0'):
    res=res.replace('.0','')
if len(res)==18:
    res=res[0:2]+'('+res[4]+')'
print(res)