def compare(string):
    for k in range(m):
        if (string[k]==stra[k]) or (stra[k]=='*') or (string[k]=='*'):
            continue
        else:
            return False
    return True

m,n = map(int,input().split())
stra = input()
strb = input()
lists = list()
for i in range(n-m+1):
#    print("{}:".format(i))
    temp = strb[i:i+m]
#    print(temp)
    place = compare(temp)
    if place:
        lists.append(i+1)
listss = [str(a) for a in lists]
strs = ' '.join(listss)
print(len(lists))
print(strs,end=' \n')