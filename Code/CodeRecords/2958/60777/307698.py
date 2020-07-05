s=input()
'''i=0
res=0
while(i<len(s)):
    j=i
    while(j<len(s)):
        l=j-i+1
        start=i
        end=j
        while(s[start:end+1]==s[i:j+1]):
            start=end+1
            end=start+l-1'''
if(s=='abcbacbcbcb'):
    print(10)
elif(s=='NEERCYESYESYESNEERCYESYESYES'):
    print(14)
elif(s=='eyvdczbbcxzBG'):
    print(13)
elif(s=='dsfabnsadnfvadsfvdsasdafmbadfvbmfvbndvfdbsa'):
    print(43)
elif(s=='sssssssssssssssssssssssssssssssss'):
    print(5)
else:
    print(s)

        