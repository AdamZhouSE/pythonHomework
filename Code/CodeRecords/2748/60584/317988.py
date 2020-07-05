def removeInvalidParentheses(s) :
        res=[]
        visited=[]
        visited.append(s)
        que=[]
        que.append(s)
        found = false
        while (not q.empty()) :
            t = q.front()
            q.pop()
            if (isValid(t)) :
            
                res.push_back(t)
                found = true
            
            if (found):
                continue
            for i in range(0,len(t)) :
                if (t[i] != '(' and t[i] != ')') :
                    continue
                str = t.substr(0, i) + t.substr(i + 1)
                if (not visited.count(str)) :
                    q.push(str)
                    visited.insert(str)

        return res

def isValid(t) :
    cnt = 0
    for i in range (0,len(t)): 
        if (t[i] == '(') :
            cnt+=1
        elif (t[i] == ')' and --cnt < 0) :
            return false
        cnt == 0
        return cnt

s=input()
print(removeInvalidParentheses(s))