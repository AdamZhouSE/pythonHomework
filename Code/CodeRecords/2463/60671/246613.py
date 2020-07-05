str1=input()
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
length=len(list0)
num=int(input())
done=False
for i in range(length-1):
    for j in range(i+1,length):
        if(list0[i]+list0[j]==num):
            print("["+str(i+1)+", "+str(j+1)+"]")
            done=True
            break
    if(done):
        break
    if(i==length-2)and(j==length-1):
        print("None")
     