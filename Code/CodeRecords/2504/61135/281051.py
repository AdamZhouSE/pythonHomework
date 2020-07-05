arrin=eval(input())
num=int(input())
arrin=sorted(arrin, key=lambda x: x[0]*x[0]+x[1]*x[1])[:num]
print(arrin)