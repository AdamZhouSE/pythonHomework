class Solution:
    def a(self, equations):
        dic = {chr(ord('a') + x): chr(ord('a') + x) for x in range(26)}
        def find(x):
            if x != dic[x]:
                dic[x] = find(dic[x])
            return dic[x]

        def Union(a, b):
            dic[find(a)] = find(b)

        equations.sort(key = lambda x : x[1], reverse = True)
        for equation in equations:
            flag = equation[1]
            if flag == '=':
                Union(equation[0], equation[-1])
            else:
                a_root = find(equation[0])
                b_root = find(equation[-1])
                if a_root == b_root:
                    return("false")
        return('true')

q=input()
q=q.replace('"','')
q=q.replace(']','')
q=q.replace('[','')
s=q.split(",")
m=Solution()
n=m.a(s)
print(n)