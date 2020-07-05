num=int(input())
str1=input()
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
length=len(list0)
temp=0
count=100
done=False
for x in list0:
    if(x>=num):
        print(1)
        done=True
        break
sum=0
for x in list0:
    sum+=x
if(sum<num):
    print(0)
    
if(not done):
    
    for i in range(length):
        sum=list0[i]
        for j in range(i+1,length):
            sum+=list0[j]
            if(sum>=num):
                temp=j-i+1
                if(temp<count):
                    count=temp
                done=True
                break
    print(count)