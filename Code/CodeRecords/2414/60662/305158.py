n = int(input())
p = 0.5
if n <=2:
    p= 1/n

elif n>=3:
    for i in range(3,n+1):
        p = (1/n)*1+(1/n)*0+((n-2)/n)*p
print("{:.5f}".format(p))