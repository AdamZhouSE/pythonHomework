num=int(input())
if num>3999 or num<1:
    print ("0")
else:
    num_tuple=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_tuple=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result=""
    for i in range(len(num_tuple)):
        while num>=num_tuple[i]:
            num-=num_tuple[i]
            result+=roman_tuple[i]
    print(result)