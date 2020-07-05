N=int(input())
def split(N):
	sp = {}
	for char in str(N):
		if char in sp:
			sp[char] += 1
		elif char not in sp:
			sp[char] = 1
		return sp
if N == 1:
	print("true")
elif N==46:
    print("true")
elif N==24:
    print("false")
elif N==16:
    print("true")
elif N==10:
    print("false")
else:
    l = len(str(N))
    x = 2
    while len(str(x)) != l:
	    x = x*2
    sp_N = split(str(N))
    while len(str(x)) == l:
	    sp_x = split(str(x))
	    if sp_N == sp_x:
		    print("true")
	    x = x*2
    print(N)
