a=input()
b=input()
li1=list(eval(a))
li2=list(eval(b))
max=0
for i in range(len(li1)):
    for j in range(len(li1)):
        value=abs(li1[i]-li1[j])+abs(li2[i]-li2[j])+abs(i-j)
        if(value>max):
            max=value
print(max)