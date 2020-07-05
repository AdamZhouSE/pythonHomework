
class Solution:
    def accountsMerge(self, accounts):
        # 先记录每一个mail对应用户名是什么
        mail2acc = {}
        for acc_info in accounts:
            for i in range(1, len(acc_info)):
                mail2acc[acc_info[i]] = [acc_info[0]]

        # 并查集
        merge_set = {}
        for mail in mail2acc.keys():
            merge_set[mail] = mail

        # 配对的mail进行归并
        for acc_info in accounts:
            for i in range(1, len(acc_info)):
                for j in range(i+1, len(acc_info)):
                    mail1 = acc_info[i]; mail2 = acc_info[j]

                    root1 = mail1
                    buf = []
                    while merge_set[root1] != root1:
                        buf.append(root1)
                        root1 = merge_set[root1]
                    for node in buf:
                        merge_set[node] = root1 # 路径压缩

                    root2 = mail2
                    buf = []
                    while merge_set[root2] != root2:
                        buf.append(root2)
                        root2 = merge_set[root2]
                    for node in buf:
                        merge_set[node] = root2  # 路径压缩

                    if root1 == root2:
                        continue

                    merge_set[root1] = root2

        for mail in mail2acc.keys():
            root = mail
            while merge_set[root] != root:
                root = merge_set[root]

            mail2acc[root].append(mail)

        ans = []
        for mail in mail2acc.keys():
            if len(mail2acc[mail]) > 1:
                tmp = mail2acc[mail][1:]
                tmp.sort()
                t = [mail2acc[mail][0]]
                t.extend(tmp)
                ans.append(t)

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
    x=Solution().accountsMerge(stones)
    print(x)