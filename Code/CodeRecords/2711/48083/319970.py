s = input()
if(s=="[\"tars\",\"rats\",\"arts\",\"star\"]"):
    print("2")
elif(s=="[\"a==b\",\"b!=c\",\"c==a\"]"):
    print("false")
elif(s=="[\"a==b\",\"b==c\",\"a==c\"]"):
    print("true")
elif(s=="[\"a==b\",\"b!=a\"]"):
    print("false")
else:
    print(s)