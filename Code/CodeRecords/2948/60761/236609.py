shortform=input("")
st=int(input(""))
num=""
for letter in shortform:
    num=num+str(st+(ord(letter)-ord('A')))
while(len(num)>2 and num!="100"):
    tempnum=""
    i=0
    while(i<len(num)-1):
        tempnum=tempnum+str((int(num[i])+int(num[i+1]))%10)
        i=i+1
    num=tempnum
print(num,end="")
