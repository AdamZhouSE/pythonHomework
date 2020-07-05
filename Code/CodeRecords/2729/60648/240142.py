ls=input().strip('[]').split(",")
#print(ls)
l=len(ls)
if ls[0]!=ls[1]:
    print(int(ls[0]))
elif ls[l-2]!=ls[l-1]:
    print(int(ls[l-1]))
else:
    for i in range(1,n-1):
        if ls[i]>ls[i-1] and ls[i]<ls[i+1]:
            print(int(ls[i]))
            break
            