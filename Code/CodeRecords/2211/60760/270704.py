firstline=list(map(int,input().split(" ")))
empresses=firstline[0]
strs=firstline[1]
letters=[]
for i in range(empresses):
    letters.append(list(input().split(" "))[0])
strss=[]
for i in range(strs):
    strss.append(input())
names=[]
onename=''
for i in letters:
    onename=i+onename
    names.append(onename)

def func(names:list,firstnames:str):
    res=0
    for i in names:
        if i.startswith(firstnames):
            res=res+1
    return res
for i in strss:
    print(func(names,i))