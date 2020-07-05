a = input().split()
l = int(a[0])
num = int(a[1])
src = input()
for i in range(num):
    points = input().split()
    rec = [int(points[0]), int(points[1])]
    num=rec[1]-rec[0]+1
    strings=[]
    for j in range(rec[0]-1,rec[1]):
        strings.append(src[:j+1])
    height=[]
    for ord in range(num-1):
        for k in range(ord+1,num):
            ans = 0
            for index in range(-1, -len(strings[ord]) - 1, -1):
                flag=0
                if strings[ord][index]==strings[k][index]:
                    flag=1
                if flag == 1:
                    ans += 1
                if flag == 0:
                    height.append(ans)
                    break
            else:
                height.append(ans)
    print(max(height))
