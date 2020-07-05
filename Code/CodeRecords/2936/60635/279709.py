tel={'A':'2','B':'2','C':'2',
     'D':'3','E':'3','F':'3',
     'G':'4','H':'4','I':'4',
     'J':'5','K':'5','L':'5',
     'M':'6','N':'6','O':'6',
     'P':'7','R':'7','S':'7',
     'T':'8','U':'8','V':'8',
     'W':'9','X':'9','Y':'9'}  # 表驱动
src={'':0}
n=int(input())
for i in range(n):
    numbers=input()
    numbers=numbers.replace('-','')
    numbers=list(numbers)
    for i,c in enumerate(numbers):
        if c.isalpha():
            numbers[i]=tel[c]
    numbers.insert(3,'-')
    numbers=''.join(numbers)
    if numbers in src:
        src[numbers]+=1
    else:
        src[numbers]=1
res=list(src.keys())
res.sort()
flag=False
for s in res:
    if src[s]>1:
        if not flag:flag=True
        print(s,src[s])
if not flag:
    print('No duplicates.',end='')