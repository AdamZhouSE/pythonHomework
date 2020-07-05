num=eval(input())
while num%4==0 and num >=4:
	num = num // 4
if num==1:
    print("true")
else:
    print("false")