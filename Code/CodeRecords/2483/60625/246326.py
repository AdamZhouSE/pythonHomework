num = int(input())

for i in range(num):
    str=input()
    patt=input()
    Index_of_patt=[]
    List_of_patt=list(patt)

    for c in patt:
        check=0
        for index in range(len(str)):
            if c == str[index]:
                Index_of_patt.append(index)
                check=1
                break
        if check==0:
            Index_of_patt.append(0)

    for j in range(len(Index_of_patt)):
        for l in range(len(Index_of_patt) - 1):
            if Index_of_patt[l] > Index_of_patt[l + 1]:
                temp = Index_of_patt[l]
                Index_of_patt[l] = Index_of_patt[l + 1]
                Index_of_patt[l + 1] = temp

                temp = List_of_patt[l]
                List_of_patt[l] = List_of_patt[l + 1]
                List_of_patt[l + 1] = temp

    res=0
    for k in range(len(Index_of_patt)):
        if Index_of_patt[k]!=0:
            print(List_of_patt[k])
            res=1
            break
    if res==0:
        print('$')