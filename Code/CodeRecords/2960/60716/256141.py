def compare(string):
    for k in range(m):
        if (string[i]==stra[i]) or (stra[i]=='*') or (string[i]=='*'):
            continue
        else:
            return False
    return True

m,n = map(int,input().split())
stra = input()
strb = input()
lists = list()
for i in range(len(strb)-len(stra)+1):
    temp = strb[i:i+len(stra)]
    place = compare(temp)
    if place:
        lists.append(i+1)
listss = [str(a) for a in lists]
strs = ' '.join(listss)
print(len(lists))
print(strs)
