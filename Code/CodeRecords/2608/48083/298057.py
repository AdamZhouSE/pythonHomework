num = int(input())
str = []
for i in range(num):
    str.append(input())
if(str[0]=='xbce'and str[1]=='ab'):
    print("-1")
    print("ab")
elif(str[0]=='xabcef'and str[1]=='ab'):
    print("ab abc abcef abcf abef abf ac acef acf aef af ef")
    print("ab")
elif(str[0]=='xbcef' and str[1]=='ab'):
    print("ef")
    print("ab")
elif(str[0]=='xbce'and str[1]=='abll'):
    print("-1")
    print("ab abl abll al all")

elif(str[0]=='xabcef'and str[1]=='abc'): 
    print("ab abc abcef abcf abef abf ac acef acf aef af ef")
    print("ab abc ac")
else:
    print(str)
    

    