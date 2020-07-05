class Solution:
    def dist(self, p1, p2):
        return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return min(self.dist(target, ghost) for ghost in ghosts) > self.dist(target, [0, 0])