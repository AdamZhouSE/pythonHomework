l=input().split(" ")
n1=int(l[0])
n2=int(l[1])
s1=input()
s2=input()
num=int(input())
for i in range(num):
    a=input().split(" ")
    b1=int(a[0])
    b2=int(a[1])
    b3=int(a[2])
    b4=int(a[3])
    str1=s1[b1-1:b2]
    #print(str1)
    str2=s2[b3-1:b4]
    #print(str2)
    sum=0
    j=0
    #print(len(str1)-len(str2))
    while j<=len(str1)-len(str2):
        '''print("j:",end=" ")
        print(j)
        print(str1[j:j+len(str2)])
        print(str2)
        print(str1[j:j+len(str2)]==str2)'''
        if str1[j:j+len(str2)]==str2:
            #print(sum)
            sum=sum+n2-j-b1
            #print("add:",end="")
            #print(n2-j-b1)
            j=j+len(str2)
            #print("3")
            #print(sum)
        else:
            j=j+1
        #print(sum)
    print(sum)