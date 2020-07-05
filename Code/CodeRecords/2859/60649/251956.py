n=int(input())
s=[]
for i in range(n):
    s.append(input())
char1=s[0][0]
char2=s[0][1]
if char1==char2:
    print("NO")
else:
    for i in range(n):
        fall = False
        subs = s[i]
        for j in range(n):
            if j == i or j == n - i - 1:
                if subs[j] == char1:
                    continue
                else:
                    fall = True
                    break
            else:
                if subs[j] == char2:
                    continue
                else:
                    fall = True
                    break
        if fall:
            print("NO")
            break
    else:
        print("YES")
