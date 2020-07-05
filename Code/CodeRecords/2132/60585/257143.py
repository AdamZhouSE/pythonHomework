from collections import Counter
s=input()
chars=Counter(s)
res=[0 for i in range(10)]
res[0]=chars['z']
res[2]=chars['w']
res[4]=chars['u']
res[6]=chars['x']
res[8]=chars['g']
res[3]=chars['r']-res[4]-res[0]
res[5]=chars['f']-res[4]
res[7]=chars['s']-res[6]
res[9]=chars['i']-res[5]-res[6]-res[8]
res[1]=chars['o']-res[0]-res[2]-res[4]
result=''
for i in range(10):
    result+=str(i)*res[i]
print(result)