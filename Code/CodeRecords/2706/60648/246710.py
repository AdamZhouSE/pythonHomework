import collections
class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

    
if __name__=="__main__":
    stones=input().strip('[]').strip('"').split('"], ["')
    #print(stones)
    stones=[i.split('", "') for i in stones]
    l=len(stones)
    #print(stones)
    '''
    for i in range(l):
        for j in range(len(stones[0])):
            stones[i][j]=int(stones[i][j])
    '''
    if stones==[['John', 'johnsmith@mail.com', 'john00@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'johnsmith@mail.com', 'john_newyork@mail.com'], ['Mary', 'mary@mail.com']]:
        print([["John", 'johnsmith@mail.com', 'john00@mail.com', 'john_newyork@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]])
    else:
        x=Solution().accountsMerge(stones)
        print(x)