#20
ori = input().split(" ")
n = int(ori[0])
m = int(ori[1])
ori = input().split(" ")
num = [int(item) for item in ori]
seq = [i for i in range(0,n)]
while len(num)>1:
    if num[0] > 0:
        num[0] -= m
    if num[0] <= 0 and len(num)>1:
        num.remove(num[0])
        seq.remove(seq[0])
        continue
    temp = num[0]
    num.remove(num[0])
    num.append(temp)
    tempS = seq[0]
    seq.remove(seq[0])
    seq.append(tempS)
print(seq[0]+1)