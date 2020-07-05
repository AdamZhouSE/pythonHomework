from fractions import Fraction
array=[]
string=input()
i=0
ans=0
while i<len(string):
    temp=['','']
    while string[i]!='/':
        temp[0]=temp[0]+string[i]
        i=i+1
    i=i+1
    while i<len(string) and string[i]!='+' and string[i]!='-':
        temp[1]=temp[1]+string[i]
        i=i+1
    ans=ans+Fraction(int(temp[0]),int(temp[1]))
if ans==int(ans):
    print(str(ans)+'/1')
else:
    print(ans)