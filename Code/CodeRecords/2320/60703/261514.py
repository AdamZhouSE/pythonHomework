STR = input()
k = int(input())
minStr  = STR
if(k==1):
    for i in range(len(STR)):
        minStr = min(minStr,minStr[1:]+minStr[0])
    print(minStr)

else:
    print("".join(sorted(STR)))