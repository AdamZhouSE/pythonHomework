class TrieNode:
    def __init__(self):
        self.nodes = dict()  # 构建字典
        self.is_leaf = False
        self.count = 1

    def insert(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            else:
                curr.nodes[char].count += 1
            curr = curr.nodes[char]
        curr.is_leaf = True

    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)

    def delete(self, word: str):
        if self.search(word) == 'YES':
            curr = self
            for char in word:
                if curr.nodes[char].count == 1:
                    del curr.nodes[char]
                    break
                curr.nodes[char].count -= 1
                curr = curr.nodes[char]

    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return 'NO'
            curr = curr.nodes[char]
        if curr.is_leaf:
            return 'YES'
        else:
            counts = 0
            for node in curr.nodes:
                counts += curr.nodes[node].count
            if curr.count > counts:
                return 'YES'
        return 'NO'

    def prefix_number(self, pre: str):
        curr = self
        for char in pre:
            if char not in curr.nodes:
                return 0
            curr = curr.nodes[char]
        return curr.count


if __name__ == '__main__':
    lines = int(input())
    t = TrieNode()
    res = []
    for i in range(lines):
        tmp = input().split()
        op = int(tmp[0])
        if op == 1:
            t.insert(tmp[1])
        elif op == 2:
            t.delete(tmp[1])
        elif op == 3:
            res.append(t.search(tmp[1]))
        else:
            res.append(t.prefix_number(tmp[1]))
    for r in res:
        print(r)