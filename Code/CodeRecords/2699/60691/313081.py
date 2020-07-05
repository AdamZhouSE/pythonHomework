import queue
MAXN = 100
MAXM = 100
s = ['']*(MAXN+5)
ok = [False]*(MAXM+5)
class Trie:
    tot = 0
    in_ = [0]*26
    e = [[0]*26]*26
    ch = [[0]*26]*(MAXM+5)
    ed = [False]*(MAXM+5)
    q = queue.Queue()
    def insert(self,x:str):
        u = 1
        l = len(x)
        for i in range(0,l):
            v = ord(x[i]) - ord('a')
            if not self.ch[u][v]:
                self.tot = self.tot + 1
                self.ch[u][v] = self.tot
            u = self.ch[u][v]
        self.ed[u] = True
    def topoSort(self):
        while not self.q.empty():
            self.q.get()
        for i in range(26):
            if not self.in_[i]:
                self.q.put(i)
        while not self.q.empty():
            u = self.q.get()
            for v in range(0,26):
                if self.e[u][v]:
                    self.in_[v]-=1
                    if not self.in_[v]:
                        self.q.put(v)
    def find(self,x:str):
        u = 1
        l = len(x)
        for i in range(l):
            if self.ed[u]:
                return 0
            v = ord(x[i])-ord('a')
            for j in range(26):
                if v!=j and self.ch[u][j] and not self.e[v][j]:
                    self.e[v][j] = 1
                    self.in_[j] += 1
            u = self.ch[u][v]
        self.topoSort()
        for i in range(26):
            if self.in_[i]:return 0
        return 1


tr = Trie()
n = eval(input())
tr.tot = 1
ans = 0
tr.in_ = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tr.e = []
for i in range(26):
    tr.e.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
tr.ch = []
for i in range(MAXM+5):
    tr.ch.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(1,n+1):
    s[i] = input()
    tr.insert(s[i])
for i in range(1,n+1):
    if tr.find(s[i]):
        ans = ans + 1
        ok[i] = True
print(ans)
for i in range(n+1):
    if ok[i]:
        print(s[i])
