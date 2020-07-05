import datetime
a=datetime.datetime.strptime(input(), '%Y-%m-%d')
b=a.replace(month=1,day=1)
print((a-b).days+1)