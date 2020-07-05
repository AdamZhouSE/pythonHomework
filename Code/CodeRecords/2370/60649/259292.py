n=int(input())
if n==0:
    print('0')
else:
    digits=[]
    while n!=0:
        n,r=divmod(n,-2)
        if r<0:
            n+=1
            r+=2
        digits.append(str(r))
    print("".join(digits[::-1]))