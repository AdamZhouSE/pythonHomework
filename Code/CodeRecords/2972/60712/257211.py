n =int(input())
sl=[]
for i in range(n):
    s1 = input()
    s2 = input()
    sl.append([s1,s2])
for m in range(n):
    l1 = list(sl[m][0])
    l2 = list(sl[m][1])
    if l1==l2:
        print('Yes')
    else:
        l = ['0'] * len(l2)
        k=0
        bl = True
        for i in range(len(l1)):
            bl = False
            for j in range(k,len(l2)):
                if len(l1) - i <= len(l2) - j:
                    if l1[i] == l2[j]:
                        l[j] = l2[j]
                        bl = True
                        k=j+1
                        break
            if bl==False:
                print('No')

                break
       # print(l)
       # print(l2)
        if bl:
            first=len(l2)
            for i in range(len(l2)):
                if l[i]!=l[0] and l[i]!='0':
                    first = i
                    break
            for i in range(len(l2)):
                if l[i]=='0':
                    if l2[i]!=l[0]:
                        l[i]=l2[i]
                    else:
                        if i>first:
                            l[i]=l2[i]
            if "".join(l)=="".join(l2):
                print('Yes')
            else:
                print('No')



