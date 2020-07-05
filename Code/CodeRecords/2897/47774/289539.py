words=eval(input())
ans = 0
dic = []
for word in words:
    dic.append(set(word))#去除重复字母
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        #找最大值
        if len(words[i]) * len(words[j]) > ans and len(dic[i] & dic[j]) == 0:#无重复字母
            ans = len(words[i]) * len(words[j])
print(ans)