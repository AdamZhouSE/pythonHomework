rom = [
	(1000,'M'), 
	(900,'CM'), 
	(500,'D'), 
	(400,'CD'), 
	(100,'C'), 
	(90,'XC'), 
	(50,'L'), 
	(40,'XL'), 
	(10,'X'), 
	(9,'IX'), 
	(5,'V'), 
	(4,'IV'), 
	(1,'I')
]
num = int(input())
result = ''
for count, sign in rom:
    if num >= count:
        n = int(num/count)
        for i in range(n):
            result += sign
        num -= n*count
print(result)