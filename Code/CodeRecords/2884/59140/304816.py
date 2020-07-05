s = input()
n, d = int(s.split(" ")[0]), int(s.split(" ")[1])
soldiers = [int(x) for x in input().split(" ")]
pairnum=0
for i in range(n):
    for j in range(n):
        if i == j: continue
        if abs(soldiers[i]-soldiers[j])<=d:pairnum+=1
print(pairnum)