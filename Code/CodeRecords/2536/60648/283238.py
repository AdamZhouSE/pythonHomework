import collections

class Solution:
    def findItinerary(self, tickets):
        paths = collections.defaultdict(list)
        for start, tar in tickets:
            paths[start].append(tar)
        for start in paths:
            paths[start].sort(reverse=True)
        s = []

        def search(start):
            while paths[start]:
                search(paths[start].pop())
            s.append(start)

        search("JFK")
        return s[::-1]
    
    
if __name__=="__main__":
    l=eval(input())
    x=Solution().findItinerary(l)
    print(x)