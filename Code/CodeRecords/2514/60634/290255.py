class Trie:
    def __init__(self):
        self.root = Node('#')

    def insert(self, word):
        poi = self.root
        i = 0
        while i <= len(word):
            if i == len(word):
                poi.count += 1
                break
            if word[i] not in poi.son:
                node = Node(word[i])
                poi.son[word[i]] = node
            poi = poi.son[word[i]]
            i += 1

    def search(self,word):
        return self.inierSearch(self.root,word,0)

    def inierSearch(self, node, word, i):
        if i == len(word):
            return True
        if word[i] in node.son:
            return self.inierSearch(node.son[word[i]],word,i + 1)
        else:
            judge = False
            for x in node.son:
                if node.son[x] != None:
                    judge = judge or self.inierSearch(node.son[x],word,i)
            return judge




class Node:
    def __init__(self, val):
        self.count = 0
        self.val = val
        self.son = {'#': None}


def solve(s,t):
    sTrie = Trie()
    for x in s:
        sTrie.insert(x)


# main-----
t = input()
s = input()
sTrie = Trie()
sTrie.insert(s)
print(sTrie.search(t))