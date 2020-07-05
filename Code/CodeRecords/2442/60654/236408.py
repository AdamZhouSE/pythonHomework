s = input().strip("[").strip("]").split(",")
if s.__len__()<2:
    print(0)
else:
    maxi = 0
    for i in range(s.__len__() - 1):
        if(int(s[i+1])-int(s[i])>maxi):
            maxi = int(s[i+1])-int(s[i])
    print(maxi)
