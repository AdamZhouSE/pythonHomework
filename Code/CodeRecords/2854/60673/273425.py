
nums = input().split(" ")
for i in range(6):
    nums[i] = int(nums[i])
firnum = 0
secnum = 0
fir = nums[0]

for i in range(6):
    if (nums[i] != nums[0]):
        sec = nums[i]
        break

# possible to be elephant

if (len(set(nums)) == 2):
    for i in range(6):
        if (nums[i] == fir):
            firnum += 1
    if (firnum == 2 or firnum == 4):
        print ("Elephant")                          
    else:
        print("Alien")

elif (len(set(nums)) == 3):
    for i in range(len(nums)):
        if (nums[i] == fir):
            firnum += 1
        elif (nums[i] == sec):
            secnum += 1

    if ((secnum == 1 and firnum == 1) or (firnum == 1 and secnum == 4) or (firnum == 4 and secnum == 1)):
        print("Bear")
    else:
        print("Alien")
        
elif(len(set(nums)) == 1):
    print ("Elephant") 
else:
    print("Alien")

