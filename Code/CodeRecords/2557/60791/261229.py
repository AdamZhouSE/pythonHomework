def solve(string):
	temp = '' + string[0]
	for i in range(len(string)-1):
		if(string[i]!=string[i+1]):
			temp += string[i+1]
	return temp
T=int(input())
x = 0
while(x<T):
    string = str(input())
    res = solve(string)
    print(res)
    x+=1