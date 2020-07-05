s=input()
res={}
res['0']=s.count('z')
res['2']=s.count('w')
res['4']=s.count('u')
res['6']=s.count('s')
res['8']=s.count('g')
res['3']=s.count('h')-res['8']
res['5']=s.count('f')-res['4']
res['7']=s.count('s')-res['6']
res['9']=s.count('i')-res['5']-res['6']-res['8']
res['1']=s.count('n')-res['7']-res['9']
output = [key * res[key] for key in sorted(res.keys())]
print(''.join(output))