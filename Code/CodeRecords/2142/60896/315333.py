a=eval(input())
for i in range(a):
    s=input()
    count1=0
    count2=0
    list1=[]
    for i in range(len(s)):
        ch=s[i]
        if(ch=='('):
            count1+=1
            count2=count1
            print(count1,end=' ')
        if(ch==')'):
            while(count2 in list1):
                count2-=1
            print(count2,end=' ')
            list1.append(count2)
            count2-=1
    print('')