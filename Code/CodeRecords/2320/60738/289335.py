strin=input()
string=strin
N=int(input())
output=""
if N>1:
    print("".join(sorted(string)))
else:
    temp=string
    for i in range(len(string)):
        string=strin[i:]+strin[:i]
        if string<temp:
            temp=string
    print(temp)
    
    
    

            
            
            