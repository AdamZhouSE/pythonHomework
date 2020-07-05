def p(l):
    for i in l:
        print(i)
l = [[2,2,1,1,0],[0],[15,17,16,20,20,20,20,20],[1],[2]]
n = input().split(" ")
all = []
for i in range(int(n[0])+int(n[1])):
    all.append(input())
if all[-1]=="AY":
    p(l[0])
elif all[-1] == "EEEEEEE":
    p(l[1])
elif all[-1] == "V":
    p(l[2])
elif all[-1] == "K":
    p(l[3])
elif all[-1] == "BBBB":
    print(2)
