temp=input().split("]")
list=eval(temp[0]+']')
n=int(temp[1].replace(", ",""))
for i in range(0,len(list)-1):
    if(list[i]<n and n<list[i+1]):
        print(i+1)
        break
    elif list[i]==n:
        print(i)
        break