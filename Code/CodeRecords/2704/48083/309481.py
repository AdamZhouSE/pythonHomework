class Solution1:
    def findRedundantConnection(self, edges):
        p = [i for i in range(len(edges) + 1)]
        p = [*range(len(edges) + 1)]      
        def f(x):
            if p[x] != x:       
                p[x] = f(p[x]) 
            return p[x]
        for x, y in edges:      
            px, py = f(x), f(y)
            if px != py:        
                p[py] = px
            else:
                return [x, y]   

if __name__ == '__main__':
    edges =input()
    s1 = Solution1()
    print(s1.findRedundantConnection(edges))