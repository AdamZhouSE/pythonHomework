a=int(input())
list1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
list2=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
index=0
while(a!=0):
    if a>=list1[index]:
        a=a-list1[index]
        print(list2[index],end="")
    else:
        index=index+1
print()