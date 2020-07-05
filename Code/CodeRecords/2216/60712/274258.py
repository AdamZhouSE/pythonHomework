import re
strl=re.split(r'([-+/])',input())
ex1=''
ex2=1
set1=set()
for i in range(len(strl)):
    if strl[i]=='/':
        set1.add(strl[i+1])
set1=list(set1)
#通分，分母
for i in range(len(set1)):
    ex2=ex2*int(set1[i])
for i in range(len(strl)):
    if strl[i]=='/':
        if i-2>=0:
            temp=strl[i-2]
            ex1 = ex1 + temp+str(int(int(strl[i - 1]) * int(ex2 / int(strl[i + 1]))))
        else:
            ex1 = ex1 + str(int(int(strl[i - 1]) * int(ex2 / int(strl[i + 1]))))
ex1=int(eval(ex1))
for i in range(len(set1)):
    if ex1%int(set1[i])==0:
        ex1 =int(ex1/int(set1[i]))
        ex2 =int(ex2/int(set1[i]))

print(str(ex1)+'/'+str(ex2))

