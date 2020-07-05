num  = int(input())
allexp = []
for i in range(num):
    n = input()
    allexp.append(input().split(" "))
for all in allexp:
    for k in range(len(all)):
        all[k] = int(all[k])
    down = -1
    res = ""
    for k in range(len(all)-1):
        if all[k]<=all[k+1] and down == -1:
            down = k
        if all[k]>all[k+1] and down != -1:
            res = res+"("+str(down)+" "+str(k)+") "
            down = -1
        elif k+2 == len(all):
            res = res + "(" + str(down) + " " + str(k+1) + ") "
    print(res[0:-1])
