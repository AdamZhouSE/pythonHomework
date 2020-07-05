x=int(input())
result=x^(x>>1)
print(result&(result+1)==0)