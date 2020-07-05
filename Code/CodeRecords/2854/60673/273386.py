nums = input().split(" ")
for i in range(6):
    nums[i] = int(nums[i])
firnum = 0
secnum = 0
thirnum = 0
fir = nums[0]
#找到第二个不同的棍子
for i in range(6):
    if (nums[i] != nums[0]):
        sec = nums[i]
        break

# possible to be elephant
if (len(set(nums)) == 2):
    for i in range(6):
        if (nums[i] == fir):
            firnum += 1
    if (firnum == 2 | firnum == 4):
        print ("Elephant")
    else:
        print("Alien")

elif (len(set(nums)) == 3):
    for i in range(len(nums)):
        if (nums[i] == fir):
            firnum += 1
        elif (nums[i] == sec):
            secnum += 1

    if ((secnum == 1 & firnum == 1) | (firnum == 1 & secnum == 4) | (firnum == 4 & secnum == 1)):
        print("Bear")
    else:
        print("Alien")
else:
    print("Alien")
