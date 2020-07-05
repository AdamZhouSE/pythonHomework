l = input()
l = int(l)
result = 0
for i in range(l):
    str1=input()
    if str1[i]==str1[-1-i]:
        count = 0
        for j in range(l):
            if j!=i and j!=-1-i and str1[j]!=str1[i]:
                count=count+1
        if i==(l-1)/2:
            if count==l-1:
                result = result + 1
            else:
                print('NO')
                break
        else:
            if count == l-2:
                result = result + 1
            else:
                print('NO')
                break
    else:
        print('NO')
        break
if result == l:
    print('YES')