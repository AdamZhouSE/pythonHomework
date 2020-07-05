n = int(input())
string = bin(n)[2:][::-1]
result =""
for i in range(len(string),64):
    string=string+"0"
list1=list(map(int,list(string)))   
for i in range(len(list1)-1):
    if list1[i]>1:  
        list1[i+1] = list1[i+1]+1
        list1[i] =list1[i]%2
    if i%2!=0:
        if list1[i] ==1:
            list1[i+1] =list1[i+1]+1
for i in range(len(list1)-1,0,-1):
    if list1[i]!=0:
        for j in range(i,-1,-1):
            result=result+str(list1[j])
        break
if n==1 or n==0:
    print(str(n))
else:
    print(result)
        
            
    