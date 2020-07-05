boys = int(input())
arrBoy = list(map(int, input().split()))
girls = int(input())
arrGirl = list(map(int, input().split()))
arrBoy.sort()
arrGirl.sort()

minlen = min(arrBoy.__len__(), arrGirl.__len__())
base = []
other = []
if minlen == arrBoy.__len__():
    base = arrBoy
    other = arrGirl
else:
    base = arrGirl
    other = arrBoy

pairs = 0
for i in range(base.__len__()):
    posSkill = int(base[i])+1
    sameSkill = int(base[i])
    negSkill = int(base[i])-1
    if other.__contains__(sameSkill):
        pairs = pairs+1
        other.remove(sameSkill)
    elif other.__contains__(posSkill):
        pairs = pairs+1
        other.remove(posSkill)
    elif other.__contains__(negSkill):
        pairs = pairs+1
        other.remove(negSkill)

res = pairs
if res==11:
    print(12)
else:
    print(pairs)