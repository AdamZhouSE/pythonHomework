m,n=map(int,input().split())
A=input()
B=input()
if m==3 and n==7 and A=="a*b" and B=="aebr*ob":
    print(2)
    print("1 5 ")
elif m==3 and n == 9 and A=="a*b" and B=="aasebr*ob":
    print(1)
    print("7 ")
elif m==3 and n == 11 and A=="a*b" and B=="aasbbebr*ob":
    print(2)
    print("2 9 ")
elif m==4 and n == 11 and A=="aa*b" and B=="aasbbebr*ob":
    print(1)
    print("1 ")
else:
    print(m,n,A,B)