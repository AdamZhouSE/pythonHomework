nums = input().split(",")
nums = list(map(int,nums))
positiveNum = []
negativeNum = []
for i in nums:
    loc = 0
    if i < 0:
        for j in range(len(negativeNum)):
            if i < negativeNum[j]:
                negativeNum.insert(j,i)
                break
        else:
            negativeNum.insert(len(negativeNum),i)
    else:
        for j in range(len(positiveNum)):
            if i > positiveNum[j]:
                positiveNum.insert(j,i)
                break
        else:
            positiveNum.insert(len(positiveNum),i)
if len(nums) == 3:
    print(nums[0]*nums[1]*nums[2])
elif len(negativeNum)<=1:
    print(positiveNum[0]*positiveNum[1]*positiveNum[2])
elif len(positiveNum)<=2:
    print(positiveNum[0]*negativeNum[1]*negativeNum[0])
else:
    if (positiveNum[1]*positiveNum[2])>(negativeNum[1]*negativeNum[0]):
        print(positiveNum[0]*positiveNum[1]*positiveNum[2])
    else:
        print(positiveNum[0]*negativeNum[1]*negativeNum[0])