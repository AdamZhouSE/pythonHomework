number=int(input(""))
scores=input("").split(" ")
way=0
nums=[0]*number
for score in scores:
	if(not int(score) in nums):
		nums[0]=int(score)
		way=way+1
print(way)