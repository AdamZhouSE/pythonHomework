import collections

beginWord=input()
endWord=input()
temp=input()
wordList=temp[2:len(temp)-2].split('","')
if endWord not in wordList or not endWord or not beginWord or not wordList:
    print('[]')
else:
    L = len(beginWord)

    # 表明dict中元素是list type
    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

    # Queue for BFS
    queue = [(beginWord, [beginWord], 1)]
    visited = {beginWord: 1}

    ans_list = []
    firstFound = True
    min_length = 0

    flag=True
    while queue:
        curr_word, curr_path, level = queue.pop(0)
        for i in range(L):
            intermediate_word = curr_word[:i] + "*" + curr_word[i + 1:]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    if firstFound:
                        min_length = level + 1
                        firstFound = False
                        ans_list.append(curr_path + [word])
                    else:
                        if level + 1 > min_length:
                            flag=False
                            break
                        else:
                            ans_list.append(curr_path + [word])
                    continue

                if word in visited and visited[word] < level + 1:
                    continue
                else:
                    visited[word] = level + 1
                    queue.append((word, curr_path + [word], level + 1))
            if not flag:break
        if not flag: break
    print('[')
    for x in ans_list:
        print("  "+str(x),end="")
        if x==ans_list[len(ans_list)-1]:print("")
        else:print(",")
    print(']')

