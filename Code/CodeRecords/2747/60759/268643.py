from re import match


def find_before(seq, idx, next_word):
    words = queue[idx][1]
    if words == [b_word]:
        # 从b_word而来，一定能连回去
        seq.append(b_word)
        ans.append(seq)
        # print(ans)
        return
    elif words == [e_word]:
        seq.append(e_word)
        find_before(seq, idx - 1, e_word)
    else:
        for word in words:
            patterns = [next_word[:i] + '[a-z]' + next_word[i + 1:] for i in range(len(next_word))]
            if any(match(pattern, word) is not None for pattern in patterns):
                save_seq = seq.copy()
                seq.append(word)
                find_before(seq, idx - 1, word)
                seq = save_seq


def judge():
    if e_word not in dic:
        return False
    else:
        for idx, current_words in queue:
            queue.append([idx + 1, []])
            for current_word in current_words:
                patterns = [current_word[:i] + '[a-z]' + current_word[i + 1:] for i in range(len(current_word))]
                for pattern in patterns:
                    # print([x for x in dic if match(pattern, x) is not None and x not in visited])
                    queue[idx + 1][1].extend([x for x in dic if match(pattern, x) is not None and x not in visited])
                    visited.update(queue[idx + 1][1])
                if e_word in queue[idx + 1][1]:
                    # print(queue)
                    return True
            else:
                if len(visited) == len(dic) and len(queue[idx + 1][1]) == 0:
                    return False
            # print(idx, visited, queue)


b_word = input()
e_word = input()
dic = eval(input())
queue = [[0, [b_word]]]
ans = []
visited = set()
visited.add(b_word)
if not judge():
    print([])
else:
    queue[len(queue) - 1][1] = [e_word]
    find_before([], len(queue) - 1, '')
    ans = list(map(lambda x: list(reversed(x)), ans))
    ans.sort()
    print(ans)
