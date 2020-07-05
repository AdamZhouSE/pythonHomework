time=eval(input())
a=0
af=0
bs=0
bf=0
for i in range(time):
	string=input()
	num=[int(n) for n in string.split()]
	if(num[0]==1):
		a=a+num[1]
		af=af+num[2]
	if(num[0]==2):
		bs=bs+num[1]
		bf=bf+num[2]
if(a>=af):
    print("LIVE")
else:
    print("DEAD")
if(bs>=bf):
    print("LIVE")
else:
    print("DEAD")