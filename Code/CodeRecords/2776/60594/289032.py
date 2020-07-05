def findAllConcatenatedWordsInADict(words):
    def check_word(word, pre_dict):
        if len(word) == 0:
            return True
        cur_dict = pre_dict
        for index, c in enumerate(word):
            cur_dict = cur_dict.get(c, None)
            if cur_dict is None:
                return False
            if cur_dict.get('end', 0) == 1:
                if check_word(word[index + 1:], pre_dict):
                    return True
        return False

    words.sort(key=lambda x: len(x))
    ans = []
    pre_dict = {}
    for item in words:
        if len(item) == 0:
            continue
        if check_word(item, pre_dict):
            ans.append(item)
        else:
            # insert word
            cur_dict = pre_dict
            for c in item:
                if cur_dict.get(c, None) is None:
                    cur_dict[c] = {}
                cur_dict = cur_dict.get(c)
            cur_dict['end'] = 1
    for index in range(len(ans)):
        for index1 in range(index+1,len(ans)):
            if ans[index][0]>ans[index1][0]:
                tmp=ans[index]
                ans[index]=ans[index1]
                ans[index1]=tmp
    return ans

oc=eval(input())
print(findAllConcatenatedWordsInADict(oc))