list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

a=input()
while(a!='!'):
    tmp=list(a)
    target=[]
    for i in tmp:
        if i in list1:
            target.append(list1[25-list1.index(i)])
        elif i in list2:
            target.append(list2[25-list2.index(i)])
        else:
            target.append(i)
    output=''
    for i in target:
        output+=i
    print(output)
    a=input()