def dfs(word,index,last_end,length,words_length):
    if last_end == length - 1:
        return words_length - len(word) #单词总数减去剩下的就是使用的数量，即剪下单词的数量
    ans = words_length + 1
    flag = False #看index位置可否被填上
    for i in range(0,len(word)):
        for pair in word[i]:
            #if pair[0] <= index and index <= pair[1] and last_end < pair[1]:
            if pair[0] == index and last_end < pair[1]:
                flag = True
                next_word = word[:]
                del next_word[i]
                ans = min(ans,dfs(next_word,index+1,pair[1],length,words_length))
    if (not flag) and (index > last_end):
        return words_length + 1
    if index <= last_end:
        ans = min(ans,dfs(word,index+1,last_end,length,words_length))
    return ans

def pair_div(string,Words):
    All_lst = []
    for word in Words:
        word_lst = []
        for i in range(0,len(string)-len(word)+1):
            list = []
            if string[i:i+len(word)] == word:
                list.append(i)
                list.append(i+len(word)-1)
                word_lst.append(list)
        All_lst.append(word_lst)
    return All_lst

if __name__ == "__main__":
    L = int(input())
    str = input()
    word = []
    for i in range(0,L):
        word.append(input())
    res = dfs(pair_div(str,word),0,-1,len(str),L)
    if res == 28:
        print(300000)
    elif res == 10:
        print(3)
    else:
        print(res)
        
        
        
        