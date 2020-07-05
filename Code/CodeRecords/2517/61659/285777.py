A=eval("["+input()+"]")
B=eval("["+input()+"]")
C=eval("["+input()+"]")
D=eval("["+input()+"]")

result=0
for x in A:
    for y in B:
        for z in C:
            for l in D:
                if x+y+z+l==0:
                    result=result+1

print(result)