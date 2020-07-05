import string

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        wordDict, step = set(wordList), 1

        if endWord not in wordDict:

            return []



        s1, s2 = set([beginWord]), set([endWord])

        while s1:

            stack = set([])

            wordDict -= s1



            for s in s1:

                for i in range(len(beginWord)):

                    for j in string.ascii_lowercase:

                        tmp = s[:i] + j + s[i+1:]

                        if tmp not in wordDict:

                            continue

                        if tmp in s2:

                            return step + 1

                        stack.add(tmp)



            if len(stack) < len(s2):

                s1 = stack

            else:

                s1, s2 = s2, stack

            step += 1

        return []



if __name__ == "__main__":

    beginWord = input()

    endWord = input()

    s=input()
    wordList=s[1:len(s)-1].split(",")

    print(Solution().ladderLength(beginWord, endWord, wordList))