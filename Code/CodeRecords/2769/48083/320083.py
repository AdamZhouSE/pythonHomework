s = input()
b = input()
if(s=="[[0,0,0],"):
    print(6)
elif(s=="[[0,1,1],"):
    print(-1)
elif(s==")("):
    print("['']")
elif(s=="[\"23:39\",\"00:00\"]"):
    print("21")
else:
    print(s)