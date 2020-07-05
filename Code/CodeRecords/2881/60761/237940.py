n=int(input(""))
j=1
while j<n:
    print("*"*int((n-j)/2)+"D"*j+"*"*int((n-j)/2))
    j=j+2
else:
    while(j>=1):
        print("*"*int((n-j)/2)+"D"*j+"*"*int((n-j)/2))
        j=j-2
    