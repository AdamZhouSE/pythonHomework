nums=input()[1:-1].split(",")
equal=[[] for i in range(len(nums)) ]
number=0
for i in nums:
    if i[2:4]=="==":
        judge=False
        for j in equal:
            if i[1] in j:
                j.append(i[4])
                judge=True
                break
            elif i[4] in j:
                j.append(i[1])
                judge=True
                break
        if judge==False:
            equal[number].append(i[1])
            equal[number].append(i[4])
            number+=1
judge = True
for i in nums:
    if i[2:4] == "!=":
        for j in equal:
            if i[1] in j and i[4] in j:
                judge=False
                break
        if judge==False:
            break
if judge==False:
    print("false")
else:
    print("true")