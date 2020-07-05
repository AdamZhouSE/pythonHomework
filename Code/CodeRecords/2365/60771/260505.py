#45
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    ori.sort()
    str_ = ""
    overlap = []
    for i in range(0,n):
        item = ori[i]
        sub = []
        sub.append(item)
        for j in range(i+1,n):
            if item in ori[j]:
                sub.append(ori[j])
            else:
                break
        if len(sub) >1:
            overlap.append(sub)
    # 把开头一样的节选出来,开始处理开头一样的部分
    if len(overlap) != 0: #说明没有开头重复的
        newStr = [] #存放所有拼好的存在重复的str
        for item in overlap:
            tar = item[0]
            item.sort(reverse=True)
            for j in range(0, len(item) - 1):
                newS = ""
                temp = item[:]
                if tar in item[j]:
                    str = item[j]
                    # print("tar2: ", str[len(tar)])
                    if int(tar[0]) > int(str[len(tar)]):
                        newS = tar + str
                        # print("tar: ",tar)
                        # print("tar2: ",str[len(tar)])
                        # print("new: ",newS)
                        temp.remove(tar)
                        temp.remove(str)
                        temp.append(newS)
                        item = temp
                        break
            item.sort(reverse=True)
            s = ""
            for i in item:
                s += i
            newStr.append(s)
        # print(newStr[0])
        for item in newStr:
            temp = ori[:]
            for i in ori:
                if item[0] == i[0]:
                    temp.remove(i)
            temp.append(item)
            ori = temp
    s = ""
    ori.sort(reverse=True)
    for item in ori:
        s += item
    print(s)