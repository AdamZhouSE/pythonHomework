def gen(n, r): 
	a = r[-1] 
	a += 1
	for i in range(1, n + 1): 
		r.append(a) 
		a += 2
	return r 

def conell(n): 
	res = [] 
	k = 1

	res.append(0) 

	while 1: 

		res = gen(k, res) 
		k += 1
		j = len(res) - 1
		while j != n and j + k > n: 
			k -= 1

		if j >= n: 
			break

	res.remove(res[0]) 
	return res 

if __name__ == "__main__": 
    count = eval(input())
    for i in range(count):
        n = eval(input())
        res = conell(n)
        for i in range(len(res) - 1):
            print(res[i], end = " ")
        print(res[len(res) - 1])
