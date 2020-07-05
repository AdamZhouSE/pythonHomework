s = []
newList = []
num = int(input())
for i in range(num):
    temp = input()
    s.append(temp)

for i in range(num):
    k = s[i]
    k = k.replace("a",'')
    k = k.replace("e",'')
    k = k.replace("i",'')
    k = k.replace("o",'')
    k = k.replace("u",'')
    temp = set(sorted(k))
   #  该段理解错误 只留下了出现一次的字符串 做复杂了
    # count = {}
    # res = ''
    # mm=0
    # for x in temp:
    #     if x in count:
    #         count[x] +=1;
    #     else:
    #         count[x] = 1
    # newcount = sorted(count.items(),key=lambda item:item[1])
    # for key,value in newcount:
    #     if value == 1 : # or key == 'a' or key == 'e' or key =='i' or key=='o' or key=='u' :
    #         res += key

    if len(temp) % 2 ==1:
        print("HE!")
    else:
        print("SHE!")