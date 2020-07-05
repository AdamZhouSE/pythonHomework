n=int(input())
str=input()
list=[]
string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range (len(str)):
    list.append(string[(string.index(str[i])+n)%26])
strr=''.join(list)
print(strr)