#06
#离谱的题目设定..
# 考虑QAAQ这种情况：是2个！（各自一个A搭配），类似的还有QAQQ
s = list(input())
count = 0
for i in range(0,len(s)):
    if s[i] != "Q":
        continue
    temp = s[:]
    j = 0
    # countA = 0
    # for c in part:
    #     if c == "A":
    #         countA += 1
    # countQ = 0
    # for c in part:
    #     if c == "Q":
    #         countQ += 1
    # count += countA*countQ
    # # 这串代码会重复计算！

    while "Q" in temp[i+1:]:
        #print("Start: ",temp[i+1:])
        j = temp.index("Q")
        temp[j] = "-"
        for item in temp[i+1:j]:
            if item == "A":
                count += 1
        #print("End: ",temp[i+1:])
print(count,end="")
