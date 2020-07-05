n=(int)(input())
for index1 in range((int)((n-1)/2)):
    for index2 in range((int)((n-(index1*2)-1)/2)):
        print("*",end='')
    for index2 in range((int)(index1*2+1)):
        print("D",end='')
    for index2 in range((int)((n-(index1*2)-1)/2)):
        print("*",end='')
    print()
for index1 in range(n):
    print("D",end='')
print()
index1=(int)((n-3)/2)
while index1!=-1:
    for index2 in range((int)((n-(index1*2)-1)/2)):
        print("*",end='')
    for index2 in range((int)(index1*2+1)):
        print("D",end='')
    for index2 in range((int)((n-(index1*2)-1)/2)):
        print("*",end='')
    print()
    index1-=1