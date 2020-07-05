
def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * func(n - 1))
    
    
    
ucnum = int(input())
ans = list()



for i in range(ucnum):
    n,m,l,r = map(int,input().split())
    strs = input().split()
    lists = [int(j) for j in strs]
    lista = [j for j in range(l,r+1)]
    listb = [lists.count(j) for j in lista]
    use = list(zip(lista,listb))
    uses = [list(i) for i in use]
    while m>0:
        uses = sorted(uses,key=lambda quality:quality[1])
        uses[0][1]+=1
        lists.append(uses[0][0])
        m-=1


    sets = list(set(lists))
    t = 1
    for ele in sets:
        t *= func(lists.count(ele))

    a = func(len(lists))

    ans.append(a//t)
for i in ans:
    print(i)