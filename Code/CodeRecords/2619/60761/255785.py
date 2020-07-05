def lucknum(num):
    if(len(num)<=1):
        return 1
    elif "1" in num or len(set(num))<len(num):
        return 0
    else:
        a=1
        numlist=[int(letter) for letter in num]
        for j in range(2,len(num)+1):
            for k in range(len(num)-j):
                for m in range(k,k+j):
                    a=a*numlist[m]
                if(a in numlist):
                    return 0
                numlist.append(a)
                a=1
        return 1

t=int(input())
for i in range(t):
    n=input()
    print(lucknum(n))
    
                