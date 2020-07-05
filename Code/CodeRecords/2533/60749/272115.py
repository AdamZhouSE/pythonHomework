str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
nums=list(map(int,str1.split(",")))
numsodd=[]
numseven=[]
for h in nums:
    if h%2==0:
        numseven.append(h)
    else:
        numsodd.append(h)
nums=numseven+numsodd
print(nums)