def compare(string):
    for k in range(m):
        try:
            if (string[i]==stra[i]) or (stra[i]=='*') or (string[i]=='*'):
                continue
            else:
                return False
        except:
            print(string)
    return True

m,n = map(int,input().split())
stra = input()
print(list(stra))
strb = input()
print(strb)
lists = list()
for i in range(len(strb)-len(stra)+1):
    temp = strb[i:i+m]
    print(temp)
    place = compare(temp)
    if place:
        lists.append(i+1)
listss = [str(a) for a in lists]
strs = ' '.join(listss)
print(len(lists))
print(strs)
