num = int(input())
temp = []
cnt = 1
ans = 0
for i in range(num):
    m = input().split(" ")
    if m[0] == "Add":
        try: 
            a=int(m[1])
        except:
            a=0
            print((m[1]))  
            continue
        b = int(m[3]) - int(m[2])
        temp.append([a, b, cnt])
        cnt += 1
    elif m[0] == "Del":
        for j in range(len(temp)):
            if temp[j][2] == int(m[1]):
                del (temp[j])
                break
    elif m[0] == "Query":
        for j in range(len(temp)):
            if temp[j][0] * int(m[1]) > temp[j][1]:
                ans += 1
            else:
                continue
        print(ans)
        ans = 0