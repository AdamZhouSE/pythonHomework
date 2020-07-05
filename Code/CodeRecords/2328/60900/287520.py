nums = input().split(',')
for i in range(0,4):
    nums[i]=int(nums[i])

st = ""
judge = True
if 2 in nums:
    st+="2"
    del nums[nums.index(2)]
elif 1 in nums:
    st+="1"
    del nums[nums.index(1)]
elif 0 in nums:
    st += "0"
    del nums[nums.index(0)]
else: judge = False
if st=="2":
    if 3 in nums:
        st+="3"
        del nums[nums.index(3)]
    elif 2 in nums:
        st+="2"
        del nums[nums.index(2)]
    elif 1 in nums:
        st += "1"
        del nums[nums.index(1)]
    elif 0 in nums:
        st += "0"
        del nums[nums.index(0)]
    else: judge = False
else:
    if max(nums)<=9:
        st+=str(max(nums))
    else:
        judge=False

st+=":"
if 5 in nums:
    st+="5"
    del nums[nums.index(5)]
elif 4 in nums:
    st+="4"
    del nums[nums.index(4)]
elif 3 in nums:
    st += "3"
    del nums[nums.index(3)]
elif 2 in nums:
    st += "2"
    del nums[nums.index(2)]
elif 1 in nums:
    st += "1"
    del nums[nums.index(1)]
elif 0 in nums:
    st += "0"
    del nums[nums.index(0)]
else: judge = False

if nums[0]>9:
    judge = False
else:
    st+=str(nums[0])

if judge ==False:
    print("")
else:
    print(st)