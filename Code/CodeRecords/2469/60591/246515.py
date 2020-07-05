def findMin(string):
    basic = list(set(string))
    min = len(basic)
    for length in range(min,len(string)):
        for start in range(0,len(string) - length + 1):
            situation = True
            for c in basic:
                if(c not in string[start:start + length]):
                    situation = False
                    break
            if(situation):
                return length

n = eval(input())
while(n!=0):
    n = n - 1
    print(findMin(input()))