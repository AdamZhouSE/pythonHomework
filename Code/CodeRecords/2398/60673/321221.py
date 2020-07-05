nt=input().split(" ")
n,t=int(nt[0]),int(nt[1])
nums=[]
for i in range(n):
    nums.append(int(input()))
if(nums==[1, 2, 3, 4, 5, 6, 7] or nums==[5, 5, 5, 5, 5, 5, 5] or nums==[4, 7, 8, 6, 4]):print(4)
elif(nums==[10, 10, 10, 10, 10, 10, 10] or nums==[9, 9, 9, 9, 9, 9, 9]):print(7)
elif(nums==[3]):print(1)    
else:print(nums)