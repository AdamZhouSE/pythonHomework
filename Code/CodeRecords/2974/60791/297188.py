def hui(s):
    if len(s)%2 == 0:
        return False
    else:
        re = True
        for i in range(int((len(s))/2)):
            if s[i] != s[len(s)-1-i]:
                re = False
                return re
        return re
            
def num1(s):
    count = 0
    check = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            
            if hui(s[i:j]) and s[i:j] not in check:
                count += 1
                check.add(s[i:j])
    return count 


def num2(s):
	count = 0
	check = set()
	for i in range(len(s)):
		for j in range(i+1,len(s)+1):
			
			if not hui(s[i:j]) and s[i:j] not in check:
				
				count += 1
				check.add(s[i:j])
	return count 
	
	
	
n = input()
s = input()
res = 0

for index in range(1,len(s)):
    s1 = s[:index]
    s2 = s[index:]
    A = num1(s1)
    B = num2(s2)
    res = max(res,A*B)
print(res)