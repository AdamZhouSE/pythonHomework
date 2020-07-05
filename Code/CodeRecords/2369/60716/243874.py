def find(pars):
    for i in tablist:
        if i[0]==pars:
            return i

def Preorder(par):
    pars = par[0]
    son1 = par[1]
    son2 = par[2]
    OrderAns.append(pars)
    if son1!='*':
        temp1 = find(son1)
        Preorder(par = temp1)
    if son2!='*':
        temp2 = find(son2)
        Preorder(par = temp2)
    return

nodenum = int(input())
tablist = list()
parlist = list()
for i in range(nodenum):
    strs = input()
    tablist.append(strs)
    a = strs[0]
    parlist.append(a)
OrderAns = list()
Preorder(par = tablist[0])
string = ''.join(OrderAns)
print(string)
