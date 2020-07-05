n=int(input())
groups = n // 4;
res = 0;
i=4
if (groups >= 1):
	res = n * (n - 1) // (n - 2) + n - 3;
	while( i < groups * 4):
		res -= (n - i)*(n - i - 1) // (n - i - 2) - (n - i - 3);
		i+=4
	p=(n - groups * 4)
	if(p==1):
		res -= 1;
	elif(p== 2):
		res -= 2;
	elif(p== 3):
		res -= 6;
else:
    p=(n - groups * 4)
    if(p==3):
        res = 6;
    elif(p== 2):
        res = 2;
    elif(p== 1):
        res = 1;
print(res)