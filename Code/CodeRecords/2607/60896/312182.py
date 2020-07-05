a=eval(input())
for i in range(a):
    s=input()
    length=len(s)
    count=0
    if(length<3): print(0)
    else:
        for i in range(0,length):
            j=3
            while(i+j<=length):
                temp=s[i:i+j]
                if(temp.count('0')==temp.count('1')==temp.count('2')):
                    count+=1
                j+=3
        print(count)