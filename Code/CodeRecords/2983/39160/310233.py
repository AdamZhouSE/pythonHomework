n = int(input())
s = input()

j = n - 1
cnt = 0
flag = 0

for i in range(j):
    for k in range(j, i, -1):
        if k==i:
            if n%2 == 0 or flag == 1:
                print('Impossible')
            flag = 1
            cnt+=n//2-i
        elif s[k] == s[i]:
            for l in range(k, j):
                s[l], s[l+1] = s[l+1], s[l]
                cnt+=1
        j-=1
        break

print(cnt)
