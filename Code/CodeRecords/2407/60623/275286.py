# 给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
# 通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
a=input()
year=int(a[0:4])
month=int(a[5:7])
day=int(a[8:])
i=1
result=0
while i<month:
	if i==1:
		result+=31
	elif i==2:
		if (year%4 == 0 and year%100 != 0) or year %400 == 0:
			result+=29
		else:
			result+=28
	elif i==3:
		result+=31
	elif i==4:
		result+=30
	elif i==5:
		result+=31
	elif i==6:
		result+=30
	elif i==7:
		result+=31
	elif i==8:
		result+=31
	elif i==9:
		result+=30
	elif i==10:
		result+=31
	elif i==11:
		result+=30
	elif i==12:
		result+=31
	i+=1
result+=day
print(result)