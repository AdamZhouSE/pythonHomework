t=int(input())
result=0
for i in range(0,t):
    
    string = input()
    patt=input()
    for j in string:
        if j in patt:
            print(str(j))
            result=1
            break
    if result==0:
        print("$")
    result=0
   