rb=input()
cards=list(map(int,input().split()))
res="";
five=cards.count(5)
zero=cards.count(0)
res="5"*(five-five%9)+"0"*zero
if(zero==0):
    print("-1")
elif(five-five%9==0):
    print("0")
else:
    print(res)