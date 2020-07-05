string=input()
if len(string)==1:
    print(ord(string[0])-64)
else:
    num=0
    num+=(ord(string[0])-64)*26
    num+=ord(string[1])-64
    print(num)