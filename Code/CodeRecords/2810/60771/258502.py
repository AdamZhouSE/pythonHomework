#41
num = int(input())
outcome = []
while num > 0:
    if num < 10:
        for i in range(0,num):
            outcome.append(1)
        break
    if num < 100:
        tar = 11
        hasMinus = False
        while hasMinus == False:
            if num < tar:
                tar -= 1
            else:
                outcome.append(tar)
                num -= tar
                hasMinus = True
        continue
    if num < 1000:
        tar = 111
        hasMinus = False
        while hasMinus == False:
            if num < tar:
                tar -= 1
            else:
                outcome.append(tar)
                num -= tar
                hasMinus = True
        continue
    if num < 10000:
        tar = 1111
        hasMinus = False
        while hasMinus == False:
            if num < tar:
                tar -= 1
            else:
                outcome.append(tar)
                num -= tar
                hasMinus = True
        continue
    if num < 100000:
        tar = 11111
        hasMinus = False
        while hasMinus == False:
            if num < tar:
                tar -= 1
            else:
                outcome.append(tar)
                num -= tar
                hasMinus = True
        continue
    if num < 1000000:
        tar = 111111
        hasMinus = False
        while hasMinus == False:
            if num < tar:
                tar -= 1
            else:
                outcome.append(tar)
                num -= tar
                hasMinus = True
        continue
print(len(outcome))
for i in range(0,len(outcome)-1):
    print(outcome[i],end=" ")
print(outcome[len(outcome)-1])