inp1 = input().split("[[")
temp1 = inp1[1].split("]]")
temp2 = temp1[0].split("],[")
ans = ",".join( str(x) for x in temp2)
temp3 = ans.split(",")
for i in range(len(temp3)):
    temp3[i] = int(temp3[i])
temp3.sort()
ans1 = ", ".join( str(x) for x in temp3)
ans1 = "[" + ans1 + "]"
print(ans1)
