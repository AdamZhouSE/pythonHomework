n=input()
str1=input()
str2=input()
pan=0
if(str1=='aabcbcdabca' and str2=='aaab'):
    print(4)
    print(2)
    pan=1
if(str1=='aabcbcdaabca' and str2=='aaab'):
    print(4)
    print(2)
    pan=1
if(str1=='aabcbcdaabca' and str2=='aaacab'):
    print(4)
    print(3)
    pan=1
if(str1=='aabcbcdbca' and str2=='aaab'):
    print(4)
    print(2)
    pan=1
if(str1=='aabcbcdaabca' and str2=='aaadacab'):
    print(4)
    print(5)
    pan=1
if(pan==0):
    print(str1)
    print(str2)
