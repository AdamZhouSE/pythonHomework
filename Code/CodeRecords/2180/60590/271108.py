s1 = input()
s2 = input()

res = 0
dist = 1
for k in range(s1.__len__()):
    for i in range(s1.__len__()):
        tempS1 = s1[i:i + dist]
        #print("tempS1: ", end="")
        #print(tempS1)
        for j in range(s2.__len__()):
            tempS2 = s2[j:j + dist]
            #print("tempS2: ", end="")
            #print(tempS2)
            if tempS2 == tempS1:
                res += 1
                #print("res: ", end="")
                #print(res)
    dist += 1

print(res, end="")