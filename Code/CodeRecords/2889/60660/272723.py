t=int(input())
l = eval('[' + input().replace(' ', ',') + ']')
result=0.00000
for i in range(t):
    result+=l[i]/100*(1/t)
print("{:.6f}".format(result*100))