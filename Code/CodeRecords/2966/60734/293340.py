case = int(input())
for i in range(case):
    n, m = input().split(' ')
    n, m = int(n), int(m)
    s = input().replace(' ','')
    t = input().replace(' ','')
    for i in range(1,len(t)):
        for j in range(i+1,len(t)):
            p1 = t[:i]
            index1 = '1 '+str(i)
            p2 = t[i:j]
            index2 = str(i+1)+' '+str(j)
            p3 = t[j:]
            index3 = str(j+1)+' '+str(len(t))
            flag = False
            if p1+p2+p3 == s:
                print('YES')
                print(index1)
                print(index2)
                print(index3)
                flag = True
                break
            elif p1+p3+p2 == s:
                print('YES')
                print(index1)
                print(index3)
                print(index2)
                flag = True
                break
            elif p2+p1+p3 == s:
                print('YES')
                print(index2)
                print(index1)
                print(index3)
                flag = True
                break
            elif p2 + p3 + p1 == s:
                print('YES')
                print(index2)
                print(index3)
                print(index1)
                flag = True
                break
            elif p3 + p1 + p2 == s:
                print('YES')
                print(index3)
                print(index1)
                print(index2)
                flag = True
                break
            elif p3 + p2 + p1 == s:
                print('YES')
                print(index3)
                print(index2)
                print(index1)
                flag = True
                break
        if flag:
            break
    if flag == False:
        print('NO')