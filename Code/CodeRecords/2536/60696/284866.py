class Solution:
    def reschedule_route(self, tickets:list)->list:
        res = ['JFK']
        start = 'JFK'
        while len(tickets) != 0:
            i = 0
            des = ''
            while i < len(tickets):
                if tickets[i][0] == start:
                    if des == '' or des > tickets[i][1]:
                        des = tickets[i][1]
                        tickets.pop(i)
                        i -= 1
                i += 1
            if des == '':
                break
            else:
                res.append(des)
                start = des
        return res


if __name__ == '__main__':
    tickets = eval(input())
    print(Solution().reschedule_route(tickets))