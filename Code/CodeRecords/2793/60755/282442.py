time = int(input().split(" ")[1])
all = input().split(" ")
res = [all[0]]
for i in range(len(all)-1):
    if int(all[i+1])-int(all[i])<=time:
        res.append(all[i+1])
    else:
        res=[all[i+1]]
if time ==0:
    print(0)
else:
    print(len(res))