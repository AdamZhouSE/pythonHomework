import itertools
def istwo(n):
	return n&(n-1)==0

num=eval(input())
list_num = list(str(num))
term = list(itertools.permutations(list_num, len(list_num)))
flag=False
for i in term:
	if i[0]!="0":
		str=""
		for j in i:
			str=str+j
		if(istwo(int(str))):
			flag=True
			break
if(flag):
    print("true")
else:
    print("false")