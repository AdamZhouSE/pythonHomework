t = int(input())
for q in range(0,t):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    S = input().replace(' ','')
    T = input().replace(' ','')
    frag = []
    i = 0
    head = True
    tail = True
    flag = True
    ref = S
    while(i < n):
        for j in range(n,i, -1):
            temp = T[i:j]
            if(temp in ref):
                if(ref.find(temp[0]) == 0 and head):
                    frag.insert(0,[i,j])
                    head = False
                elif(ref.rfind(temp[-1]) == n - 1 and tail):
                    frag.append([i,j])
                    tail = False
                else:
                    if(frag == []):
                        frag.append([i,j])
                    else:
                        frag.insert(1,[i,j])
                ref = ref.replace(temp,'-',1)
                i = j
                break
        else:
            print('NO')
            flag = False
            break
    if(flag):
        if(len(frag) > 3 or len(frag) == 0):
            print('NO')
        elif(len(frag) == 3):
            print('YES')
            for item in frag:
                print(item[0] + 1,item[1])
        elif(len(frag) == 2):
            print('YES')
            for item in frag:
                if(item[0] == item[1] - 1):
                    print(item[0] + 1,item[1])
                else:
                    print(item[0] + 1,item[0] + 1)
                    print(item[0] + 2,item[1])
        else:
            print('YES')
            print(1,n - 2)
            print(n - 1,n - 1)
            print(n,n)