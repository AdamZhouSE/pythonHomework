#18
def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater %y ==0 :
            lcm = greater
            break
        greater += 1
    return lcm

# print(lcm(648,864))
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
dup = []
flag = True
for item in num:
    if item not in dup:
        dup.append(item)
dup.sort()
for i in range(0,len(dup)):
    tar = dup[i]
    for j in range(i,len(dup)):
        LCM = lcm(tar,dup[j])
        if not ( (LCM//tar == 1) or ((LCM//tar)%2 == 0 ) or ((LCM//tar)%3 == 0) ):
            flag = False
            break
    if flag == False:
        break
if flag:
    print("Yes")
else:
    print("No")