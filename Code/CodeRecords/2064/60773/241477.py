dic={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}
s=input()
n=len(s)
sum=0
for i in range(n):
    sum=sum+dic[s[i]]
    if i>=1:
        if (s[i-1]=='I')and(s[i]=='V'):sum=sum-2
        elif (s[i-1]=='I')and(s[i]=='X'):sum=sum-2
        elif (s[i - 1] == 'X') and (s[i] == 'L'):sum = sum - 20
        elif (s[i - 1] == 'X') and (s[i] == 'C'): sum = sum - 20
        elif (s[i - 1] == 'C') and (s[i] == 'D'):sum = sum - 200
        elif (s[i - 1] == 'C') and (s[i] == 'M'):sum = sum - 200
        else:sum=sum
print(sum)