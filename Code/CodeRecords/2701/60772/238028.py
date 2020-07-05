class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        def checkwin(S):
            for win in wins:
                flag = True
                for pos in win:
                    if pos not in S:
                        flag = False
                        break
                if flag:
                    return True
            return False

        A, B = set(), set()
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0:
                A.add((x, y))
                if checkwin(A):
                    return "A"
            else:
                B.add((x, y))
                if checkwin(B):
                    return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game/solution/zhao-chu-jing-zi-qi-de-huo-sheng-zhe-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。