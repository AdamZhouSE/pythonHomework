def r(s):
    a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
    sum=0
    for i in range(0, len(s)):
        if (i < len(s)-1) and (a[s[i]] < a[s[i+1]]):
            sum=sum-a[s[i]]
        else:
            sum=sum+a[s[i]]
    return sum
print(r(str(input())))