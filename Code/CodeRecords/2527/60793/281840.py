temp1 = list(input()[2:-2].split("],["))
#temp1 = ['1,4,1,40,10', '2,8,0,50,5', '3,8,1,30,4', '4,10,0,10,3', '5,1,1,15,1']
ls = [list(map(int, x.split(","))) for x in temp1]
t1, t2, t3 = int(input()), int(input()), int(input())
after = []
for x in ls:
    if (t1 == 1 and x[2] == 0) or x[3] > t2 or x[4] > t3:
        continue
    after.append(x)
after = sorted(after, key=lambda x: x[1], reverse=True)
for j in range(1, len(after)):
    for i in range(1, len(after)):
        if after[i - 1][1] == after[i][1] and after[i - 1][0] < after[i-1][1]:
            after[i - 1], after[i] = after[i], after[i - 1]
result = [x[0] for x in after]
print(result)