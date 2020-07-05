A = input()
B = input()
index = A.find(B)
count = 0
while index != -1:
	count += 1
	index = A.find(B,index+1)
print(count,end="")